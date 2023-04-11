import cv2 as cv
import numpy as np
import mediapipe as mp


HAAR_CASCADE_PATH = "haarcascade_frontalface_alt.xml"
CAMERA_INDEX = 0

mp_face_mesh = mp.solutions.face_mesh
LEFT_EYE = [362, 382, 381, 380, 374, 373, 390,    249, 263, 466, 388, 387, 386, 385, 384, 398]
# right eyes indices
RIGHT_EYE = [33, 7, 163, 144, 145, 153, 154,    155, 133, 173, 157, 158, 159, 160, 161, 246]
LEFT_IRIS = [474, 475, 476, 477]
RIGHT_IRIS = [469, 470, 471, 472]

def detect_faces(_image):
    detected_outcome = ''
    try:
        _faces = []
        cascade = cv.CascadeClassifier(HAAR_CASCADE_PATH)
        detected = cascade.detectMultiScale(
            _image, 1.3, 4, cv.CASCADE_SCALE_IMAGE, (20, 20))
        if len(detected) > 0:
            detected_outcome = ''
            for (x, y, w, h) in detected:
                _faces.append((x, y, w, h))
            return _faces, detected_outcome
        else:
            detected_outcome = 'Cheating detected'
            return _faces, detected_outcome
    except Exception as e:
        print('Error: '+str(e))

if __name__ == "__main__":
    cv.namedWindow("Video")
    font = cv.FONT_HERSHEY_SIMPLEX
    capture = cv.VideoCapture(CAMERA_INDEX)
    faces = []

    i = 0
    c = -1
    with mp_face_mesh.FaceMesh(max_num_faces=1, refine_landmarks=True, min_detection_confidence=0.5, min_tracking_confidence=0.5) as face_mesh:
        while c == -1:
            retval, image = capture.read()
            if not retval:
                break
            else:
                if i % 5 == 0:
                    faces, detected_outcome = detect_faces(image)
                    print('detected_outcome:', detected_outcome)
                cv.putText(image, detected_outcome, (50, 50), font, 1, (0, 0, 0), 2, cv.LINE_4)
                for (x, y, w, h) in faces:
                    cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

                image = cv.flip(image, 1)
                rgb_image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
                img_h, img_w = image.shape[:2]
                results = face_mesh.process(rgb_image)
                if results.multi_face_landmarks:
                    mesh_points = np.array(
                        [np.multiply([p.x, p.y], [img_w, img_h]).astype(int) for p in results.multi_face_landmarks[0].landmark])
                    (l_cx, l_cy), l_radius = cv.minEnclosingCircle(mesh_points[LEFT_IRIS])
                    (r_cx, r_cy), r_radius = cv.minEnclosingCircle(mesh_points[RIGHT_IRIS])
                    center_left = np.array([l_cx, l_cy], dtype=np.int32)
                    center_right = np.array([r_cx, r_cy], dtype=np.int32)
                    cv.circle(image, center_left, int(l_radius), (255, 0, 255), 1, cv.LINE_AA)
                    cv.circle(image, center_right, int(r_radius), (255, 0, 255), 1, cv.LINE_AA)
                image = cv.flip(image, 1)
                cv.imshow("Video", image)
                i += 1
                c = cv.waitKey(1)
                if c == 27:
                    break

    capture.release()
    cv.destroyAllWindows()
        