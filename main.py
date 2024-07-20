import cv2
import mediapipe as mp
import time
import controller as cnt

# Give the Arduino time to reset
time.sleep(2.0)

mp_draw = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands

video = cv2.VideoCapture(0)

def detect_asl_letter(lmList):
    if len(lmList) == 0:
        return ''
    
    thumb_tip = lmList[4]
    index_tip = lmList[8]
    middle_tip = lmList[12]
    ring_tip = lmList[16]
    pinky_tip = lmList[20]
    
    thumb_ip = lmList[3]
    index_dip = lmList[7]
    middle_dip = lmList[11]
    ring_dip = lmList[15]
    pinky_dip = lmList[19]
    
    # Example: Detecting 'H' (Index and middle fingers extended)
    if (index_tip[2] < index_dip[2] and
        middle_tip[2] < middle_dip[2] and
        ring_tip[2] > ring_dip[2] and
        pinky_tip[2] > pinky_dip[2]):
        return 'H'

    # Example: Detecting 'I' (Pinky extended)
    if (index_tip[2] > index_dip[2] and
        middle_tip[2] > middle_dip[2] and
        ring_tip[2] > ring_dip[2] and
        pinky_tip[2] < pinky_dip[2]):
        return 'I'

    # Example: Detecting 'E' (Fingers slightly curved inwards)
    if (abs(index_tip[2] - index_dip[2]) < 20 and
        abs(middle_tip[2] - middle_dip[2]) < 20 and
        abs(ring_tip[2] - ring_dip[2]) < 20 and
        abs(pinky_tip[2] - pinky_dip[2]) < 20 and
        abs(thumb_tip[2] - thumb_ip[2]) < 30):
        return 'E'

    # Example: Detecting 'L' (Thumb and index fingers extended, forming an 'L' shape)
    if (index_tip[2] < index_dip[2] and
        middle_tip[2] > middle_dip[2] and
        ring_tip[2] > ring_dip[2] and
        pinky_tip[2] > pinky_dip[2] and
        thumb_tip[2] < thumb_ip[2]):
        return 'L'
    
    # Example: Detecting 'Y' (Thumb and pinky extended, other fingers folded)
    if (index_tip[2] > index_dip[2] and
        middle_tip[2] > middle_dip[2] and
        ring_tip[2] > ring_dip[2] and
        pinky_tip[2] < pinky_dip[2] and
        thumb_tip[2] < thumb_ip[2] and
        abs(pinky_tip[2] - pinky_dip[2]) < 20 and
        abs(index_tip[2] - index_dip[2]) > 50):
        return 'Y'
    
    
    return ''


with mp_hand.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while True:
        ret, image = video.read()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        lmList = []
        if results.multi_hand_landmarks:
            for hand_landmark in results.multi_hand_landmarks:
                myHands = results.multi_hand_landmarks[0]
                for id, lm in enumerate(myHands.landmark):
                    h, w, c = image.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append([id, cx, cy])
                mp_draw.draw_landmarks(image, hand_landmark, mp_hand.HAND_CONNECTIONS)
        
        if len(lmList) != 0:
            asl_letter = detect_asl_letter(lmList)
            if asl_letter:
                cnt.lcd(asl_letter)
                cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, asl_letter, (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)
                cv2.putText(image, "ASL", (100, 375), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)
        
        cv2.imshow("Frame", image)
        k = cv2.waitKey(1)
        if k == ord('q'): # q to end video
            break

video.release()
cv2.destroyAllWindows()
cnt.close_serial()  # Ensure the serial port is closed when the program exits