# Arduino-LCD-ASL-Detection

Extending on from my finger counter LCD control, I used MediaPipe's Hand Landmark CNN along with OpenCV's video processing and computer vision functions to create a real-time ASL detection script that transfers the data to an LCD display connected to an Arduino Uno, when then displays the corresponding letter!

The current script only works with a handful of letters, the next steps are to train the model on all 26 letters!