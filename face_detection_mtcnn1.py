import cv2
import os
import numpy as np
from mtcnn import MTCNN
import face_recognition

# Έλεγχος για τα αρχεία .dat
MODEL_PATH = "models"
SHAPE_PREDICTOR_PATH = os.path.join(MODEL_PATH, "shape_predictor_68_face_landmarks.dat")
FACE_RECOGNITION_MODEL_PATH = os.path.join(MODEL_PATH, "dlib_face_recognition_resnet_model_v1.dat")

if not os.path.exists(SHAPE_PREDICTOR_PATH) or not os.path.exists(FACE_RECOGNITION_MODEL_PATH):
    print("Τα απαραίτητα αρχεία δεν βρέθηκαν.")
    exit()

print("Τα αρχεία βρέθηκαν επιτυχώς!")

# Φόρτωση γνωστών προσώπων
KNOWN_FACES_PATH = "known_faces"
if not os.path.exists(KNOWN_FACES_PATH):
    print("Ο φάκελος γνωστών προσώπων δεν βρέθηκε.")
    exit()

known_encodings = []
known_names = []

# Για κάθε φάκελο (όνομα ατόμου) στον φάκελο known_faces
for person_name in os.listdir(KNOWN_FACES_PATH):
    person_folder = os.path.join(KNOWN_FACES_PATH, person_name)

    if not os.path.isdir(person_folder):
        continue  # Αγνόησε αρχεία που δεν είναι φάκελοι

    # Επεξεργασία κάθε εικόνας στον φάκελο
    for image_name in os.listdir(person_folder):
        image_path = os.path.join(person_folder, image_name)
        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)

        if len(encodings) > 0:
            known_encodings.append(encodings[0])
            known_names.append(person_name)  # Το όνομα είναι το όνομα του φακέλου

print(f"Φορτώθηκαν {len(known_encodings)} γνωστά πρόσωπα από πολλαπλές εικόνες.")

# Επιλογή εισόδου
choice = input("Πατήστε 1 για κάμερα ή 2 για αποθηκευμένο βίντεο: ")
if choice == "1":
    video_source = 0  # Κάμερα
elif choice == "2":
    video_source = "C:/Project/video/export_1713300134091.MP4".strip()
    if not os.path.exists(video_source):
        print(f"Το αρχείο βίντεο δεν βρέθηκε στο μονοπάτι: {video_source}")
        exit()
else:
    print("Μη έγκυρη επιλογή.")
    exit()

# Έναρξη βίντεο
video_capture = cv2.VideoCapture(video_source)
detector = MTCNN()

while video_capture.isOpened():
    ret, frame = video_capture.read()
    if not ret:
        print("Δεν είναι δυνατή η ανάγνωση από την πηγή.")
        break

    # Μετατροπή του καρέ σε ασπρόμαυρο
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_color = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)

    # Ανίχνευση προσώπων
    results = detector.detect_faces(frame)
    for result in results:
        x, y, width, height = result['box']
        x, y = abs(x), abs(y)
        x2, y2 = x + width, y + height

        face = frame[y:y2, x:x2]
        face_encoding = face_recognition.face_encodings(face)

        name = "Άγνωστος"
        if len(face_encoding) > 0:
            matches = face_recognition.compare_faces(known_encodings, face_encoding[0])
            if True in matches:
                match_index = matches.index(True)
                name = known_names[match_index]

        # Σχεδίαση πλαισίου και εμφάνιση ονόματος
        cv2.rectangle(gray_frame_color, (x, y), (x2, y2), (0, 255, 0), 2)
        cv2.putText(
            gray_frame_color,
            name,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2,
            lineType=cv2.LINE_AA
        )

    # Προβολή βίντεο
    cv2.imshow("Αναγνώριση Προσώπων", gray_frame_color)

    # Έξοδος με 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Καθαρισμός
video_capture.release()
cv2.destroyAllWindows()
