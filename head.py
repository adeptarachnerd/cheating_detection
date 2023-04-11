import cv2

HAAR_CASCADE_PATH = "haarcascade_frontalface_alt.xml"
CAMERA_INDEX = 0


def detect_faces(_image):
	_faces = []

	detected = cascade.detectMultiScale(_image, 1.3, 4, cv2.CASCADE_SCALE_IMAGE, (20, 20))
	print(detected)

	if len(detected) > 0:
		for (_x, _y, _w, _h) in detected: 
			_faces.append((_x, _y, _w, _h))
	return _faces

	
if __name__ == "__main__":
	cv2.namedWindow("Video")

	capture = cv2.VideoCapture(CAMERA_INDEX)	
	cascade = cv2.CascadeClassifier(HAAR_CASCADE_PATH)

	faces = []

	i = 0
	c = -1
	while c == -1:
		retval, image = capture.read()

		if not retval:
			#print("camera not found")
			pass
		else:
			if i % 5 == 0:
				faces = detect_faces(image)

			for (x, y, w, h) in faces:
				cv2.rectangle(image, (x, y), (x + w, y + h), 255)

			cv2.imshow("Video", image)

		i += 1
		c = cv2.waitKey(1)
		if c == 27:
			break

	capture.release()
	cv2.destroyAllWindows()