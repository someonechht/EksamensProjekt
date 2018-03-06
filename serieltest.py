import serial
import threading
import sys

def read_stream(ser):
  while True:
    if ser.inWaiting() > 0:
      do_some_thing(ser.readline())

def do_some_thing(line):
  print(line)

dev = '/dev/ttyUSB0'
if len(sys.argv) >= 1:
  dev = sys.argv[0]

ser = serial.Serial(dev, 38400, timeout=0)

thread = threading.Thread(target=read_stream, args=(ser,))
thread.daemon = True
thread.start()

while True:
  input = raw_input('$: ')
  ser.write(input)