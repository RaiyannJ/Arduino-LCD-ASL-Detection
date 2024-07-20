import serial
import serial.tools.list_ports

ser = serial.Serial('/dev/cu.usbmodem101', 9600, timeout=1)

def lcd(letter):
    try:
        ser.write(f"{letter}\n".encode())
        print(f"Sent to Arduino: {letter}")
    except serial.SerialException as e:
        print(f"Error writing to serial port: {e}")

def close_serial():
    ser.close()
    print("Serial port closed.")
