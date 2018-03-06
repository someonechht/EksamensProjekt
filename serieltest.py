import serial
import threading


def read_stream(ser):
  while True:
    if ser.inWaiting() > 0:
      do_some_thing(ser.readline())

def do_some_thing(line):
  print(line)

ser = serial.Serial('/dev/ttyUSB0', 38400, timeout=0)

thread = threading.Thread(target=read_stream, args=(serial_port,))
thread.start()