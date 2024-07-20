import serial
import serial.tools.list_ports

ser = serial.Serial('/dev/tty.usbmodem1101', 9600, timeout=1)

def led(total):
    try:
        ser.write(f"{total}\n".encode())
        print(f"Sent to Arduino: {total}")
    except serial.SerialException as e:
        print(f"Error writing to serial port: {e}")

def close_serial():
    ser.close()
    print("Serial port closed.")
