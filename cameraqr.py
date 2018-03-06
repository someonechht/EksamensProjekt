from io import BytesIO
from time import sleep
import picamera
from PIL import Image
import zbar
import numpy


# Create a bytestream to store the image temporarily
stream = BytesIO()

# Create the scanner
scanner = zbar.Scanner()

with picamera.PiCamera() as camera:
	# Scaledown the resolution by 100 or 10 on each axis
	camera.resolution = (camera.resolution[0] // 6, camera.resolution[1] // 6)
	for foo in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
		print("Reading...")
		# We want to reuse the byte stream
		stream.seek(0)
		camera.capture(stream, format='jpeg')
		
		pil = Image.open(stream)
		pil = pil.convert('L')

		results = scanner.scan(numpy.array(pil))

		# extract results
		for result in results:
			# do something useful with results
			print('decoded {} symbol "{}"'.format(result.type, result.data))
	