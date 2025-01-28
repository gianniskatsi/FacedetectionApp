import cv2
import face_recognition
import os
import numpy as np

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

for person_name in os.listdir(KNOWN_FACES_PATH):
    person_folder = os.path.join(KNOWN_FACES_PATH, person_name)
    if not os.path.isdir(person_folder):
        continue
    for image_name in os.listdir(person_folder):
        image_path = os.path.join(person_folder, image_name)
        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)
        if len(encodings) > 0:
            known_encodings.append(encodings[0])
            known_names.append(person_name)

print(f"Φορτώθηκαν {len(known_encodings)} γνωστά πρόσωπα από πολλαπλές εικόνες.")

choice = input("Πατήστε 1 για κάμερα ή 2 για αποθηκευμένο βίντεο: ")
if choice == "1":
    video_source = 0
elif choice == "2":
    video_source = input("Δώστε το πλήρες μονοπάτι του βίντεο: ").strip()
    if not os.path.exists(video_source):
        print(f"Το αρχείο βίντεο δεν βρέθηκε στο μονοπάτι: {video_source}")
        exit()
else:
    print("Μη έγκυρη επιλογή.")
    exit()

video_capture = cv2.VideoCapture(video_source)
frame_count = 0

while video_capture.isOpened():
    ret, frame = video_capture.read()
    if not ret:
        print("Δεν είναι δυνατή η ανάγνωση από την πηγή.")
        break

    # Μετατροπή του καρέ σε ασπρόμαυρο
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Ανίχνευση προσώπων σε ασπρόμαυρο καρέ
    face_locations = face_recognition.face_locations(gray_frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    matches_names = []
    for face_encoding in face_encodings:
        face_distances = face_recognition.face_distance(known_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        
        # Προσθήκη λογικής ελέγχου για σωστή αντιστοιχία
        if face_distances[best_match_index] < 0.6:  # 0.6 threshold για το πόσο κοντά είναι η αντιστοιχία
            name = known_names[best_match_index]
        else:
            name = "Άγνωστος"
        
        matches_names.append(name)

    # Μετατροπή καρέ σε έγχρωμο για σχεδιασμό
    color_frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)

    for (top, right, bottom, left), name in zip(face_locations, matches_names):
        cv2.rectangle(color_frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(color_frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    cv2.imshow("Αναγνώριση Προσώπων", color_frame)
    frame_count += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
