import serial
import threading
import sys
import time

def read_stream(ser):
  while ser.is_open:
    if ser.in_waiting > 0:
      do_some_thing(ser.readline())

def do_some_thing(line):
  print(line.decode())

ser = serial.Serial('/dev/ttyUSB0', 38400, timeout=0)

thread = threading.Thread(target=read_stream, args = (ser,), daemon = True)
thread.start()

while True:
  result = input("$: ")
  ser.write(result.encode() + b"\r\n")
