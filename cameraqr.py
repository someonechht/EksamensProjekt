from io import BytesIO
from time import sleep
import picamera
from PIL import Image
import zbar

running = True

# Create a bytestream to store the image temporarily
stream = BytesIO()

# Create the scanner
scanner = zbar.ImageScanner()
scanner.parse_config('enable')

with picamera.PiCamera() as camera:
	# Scaledown the resolution by 100 or 10 on each axis
	camera.resolution = (camera.resolution[0] / 6, camera.resolution[1] / 6)
	while running:
		print("Reading...")
		# We want to reuse the byte stream
		stream.seek(0)
		camera.capture(stream, format='jpeg')
		
		pil = Image.open(stream)
		pil = pil.convert('L')
		width, height = pil.size
		raw = pil.tobytes()

		image = zbar.Image(width, height, 'Y800', raw)

		scanner.scan(image)
		
		# extract results
		for symbol in image:
			# do something useful with results
			print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data
	