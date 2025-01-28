from mtcnn.mtcnn import MTCNN
import cv2
import os
import numpy as np

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
        image = cv2.imread(image_path)
        detector = MTCNN()
        results = detector.detect_faces(image)

        if len(results) > 0:
            box = results[0]['box']
            x, y, width, height = box
            face = image[y:y + height, x:x + width]
            face_encoding = np.mean(face, axis=(0, 1))  # Υπολογισμός encoding με το μέσο όρο RGB
            known_encodings.append(face_encoding)
            known_names.append(person_name)

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

    # Ανίχνευση προσώπων στο καρέ
    results = detector.detect_faces(frame)

    # Σχεδίαση πλαισίων και αναγνώριση προσώπων
    for result in results:
        box = result['box']
        x, y, width, height = box
        face = frame[y:y + height, x:x + width]

        # Υπολογισμός encoding του ανιχνευμένου προσώπου
        if face.shape[0] > 0 and face.shape[1] > 0:  # Αποφυγή σφαλμάτων
            face_encoding = np.mean(face, axis=(0, 1))  # Υπολογισμός encoding με το μέσο όρο RGB

            # Αναγνώριση προσώπου
            distances = np.linalg.norm(known_encodings - face_encoding, axis=1)
            min_distance_index = np.argmin(distances)
            if distances[min_distance_index] < 0.6:  # Κατώφλι αναγνώρισης
                name = known_names[min_distance_index]
            else:
                name = "Άγνωστος"

            # Σχεδίαση πλαισίων και ονόματος
            cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 0, 255), 2)
            cv2.putText(
                frame,
                name,
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

    # Προβολή βίντεο
    cv2.imshow("Αναγνώριση Προσώπων με MTCNN", frame)

    # Έξοδος με 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Καθαρισμός
video_capture.release()
cv2.destroyAllWindows()
