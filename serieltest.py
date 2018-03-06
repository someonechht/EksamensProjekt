import serial
import threading
import sys
import time

def command(ser, s):
  try:   
    ser.flushInput()
    ser.flushOutput()
    for ch in s:
      ser.write(ch)
      time.sleep(0.001)
    ser.write('\r')  
    time.sleep(0.05)
    #while ser.inWaiting() > 0:
    for i in range(3):
      print(ser.readline())
  except Exception as e:
    print "Error: {0}".format(e)
    exit(0)

def read_stream(ser):
  while True:
    if ser.inWaiting() > 0:
      do_some_thing(ser.readline())

def do_some_thing(line):
  print(line)

ser = serial.Serial('/dev/ttyUSB0', 38400, timeout=0)

thread = threading.Thread(target=read_stream, args=(ser,))
thread.daemon = True
thread.start()

while True:
  input = raw_input('$: ')
  command(ser, input)