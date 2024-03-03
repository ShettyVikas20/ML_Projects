import cv2
from deepface import DeepFace
import dlib

# Choose the face detection method (0 for Haar Cascade, 1 for Dlib)
face_detection_method = 0

if face_detection_method == 0:
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
elif face_detection_method == 1:
    detector = dlib.get_frontal_face_detector()
else:
    raise ValueError("Invalid face detection method. Use 0 for Haar Cascade or 1 for Dlib.")

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not video.isOpened():
    raise IOError("Cannot open webcam")

while video.isOpened():
    _, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if face_detection_method == 0:
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    elif face_detection_method == 1:
        faces = detector(gray)

    for face in faces:
        if face_detection_method == 0:
            x, y, w, h = face
        elif face_detection_method == 1:
            x, y, w, h = face.left(), face.top(), face.width(), face.height()

        image = cv2.rectangle(frame, (x, y), (x + w, y + h), (89, 2, 236), 1)

        try:
            analyze = DeepFace.analyze(frame, actions=['emotion'])
            cv2.putText(image, analyze[0]['dominant_emotion'], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (224, 77, 176), 2)
            print(analyze[0]['dominant_emotion'])
        except:
            print('No face detected or error during emotion analysis')

    cv2.imshow('Video', frame)

    # Break the loop when 'q' is pressed
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
