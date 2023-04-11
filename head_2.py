import cv2

HAAR_CASCADE_PATH = "haarcascade_frontalface_alt.xml"
CAMERA_INDEX = 0


def detect_faces(_image):
	detected_outcome = ''
	try:
		_faces = []
		detected = cascade.detectMultiScale(_image, 1.3, 4, cv2.CASCADE_SCALE_IMAGE, (20, 20))
		# print(detected)
		if len(detected) > 0:
			detected_outcome = ''
			# print("len(detected) > 0: "+str(detected))
			for (x, y, w, h) in detected: 
				_faces.append((x, y, w, h))
			return _faces,detected_outcome
		else:
			detected_outcome = 'Cheating detected'
			# print("len(detected) < 0: "+str(detected))
			return _faces,detected_outcome
	except Exception as e:
		print(str(e))

	
if __name__ == "__main__":
	cv2.namedWindow("Video")
	font = cv2.FONT_HERSHEY_SIMPLEX
	capture = cv2.VideoCapture(CAMERA_INDEX)	
	cascade = cv2.CascadeClassifier(HAAR_CASCADE_PATH)
	faces = []
    
	i = 0
	c = -1
    # font = cv2.FONT_HERSHEY_SIMPLEX
    
	while c == -1:
		retval, image = capture.read()

		if not retval:
#print("camera not found")
			pass
		else:
			if i % 5 == 0:
				faces = detect_faces(image)
			# font = cv2.FONT_HERSHEY_SIMPLEX
			print(faces)
			cv2.putText(image, faces[1], (50, 50), font, 1, (0, 255, 255), 2, cv2.LINE_4)
			for (x, y, w, h) in faces[0]:
				cv2.rectangle(image, (x, y), (x + w, y + h), 255)
				
			cv2.imshow("Video", image)

		i += 1
		c = cv2.waitKey(1)
		if c == 27:
			break

	capture.release()
	cv2.destroyAllWindows()