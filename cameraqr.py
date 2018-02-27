from io import BytesIO
from time import sleep, time
import picamera
from PIL import Image
import zbar

running = True

stream = BytesIO()
scanner = zbar.ImageScanner()

scanner.parse_config('enable')

last = time()
print(time() - last)
with picamera.PiCamera() as camera:
	camera.resolution = (camera.resolution[0] / 4, camera.resolution[1] / 4)
	while running:
		stream.seek(0)
		camera.capture(stream, format='jpeg')
		pil = Image.open(stream)

		pil = pil.convert('L')
		width, height = pil.size
		raw = pil.tobytes()

		# wrap image data
		image = zbar.Image(width, height, 'Y800', raw)

		# scan the image for barcodes
		scanner.scan(image)
		
		# extract results
		for symbol in image:
			# do something useful with results
			print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data
	