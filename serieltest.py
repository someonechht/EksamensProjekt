import serial
import threading

commands = []

def read_stream(ser):
  while True:
    if ser.inWaiting() > 0:
      do_some_thing(ser.readline())

def do_some_thing(line):
  commands.append(line)
  print(commands)

ser = serial.Serial('/dev/ttyUSB0', 38400, timeout=0)

thread = threading.Thread(target=read_stream, args=(ser,))
thread.start()