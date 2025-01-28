import cv2
import face_recognition
import os
import numpy as np
from scipy.ndimage import rotate  # Για περιστροφή εικόνων

# Περιστροφή εικόνας
def augment_image(image, angles=[-30, -15, 0, 15, 30]):
    augmented_images = []
    for angle in angles:
        rotated_image = rotate(image, angle, reshape=False, mode='nearest')
        augmented_images.append(rotated_image)
    return augmented_images

# Φόρτωση γνωστών προσώπων
def load_known_faces(known_faces_path):
    known_encodings = []
    known_names = []

    for person_name in os.listdir(known_faces_path):
        person_folder = os.path.join(known_faces_path, person_name)

        if not os.path.isdir(person_folder):
            continue

        for image_name in os.listdir(person_folder):
            image_path = os.path.join(person_folder, image_name)
            image = face_recognition.load_image_file(image_path)

            # Δημιουργία παραλλαγών της εικόνας
            augmented_images = augment_image(image)
            for augmented_image in augmented_images:
                encodings = face_recognition.face_encodings(augmented_image)
                if len(encodings) > 0:
                    known_encodings.append(encodings[0])
                    known_names.append(person_name)

    return known_encodings, known_names

# Έλεγχος για τα αρχεία .dat
MODEL_PATH = "models"
KNOWN_FACES_PATH = "known_faces"

if not os.path.exists(KNOWN_FACES_PATH):
    print("Ο φάκελος γνωστών προσώπων δεν βρέθηκε.")
    exit()

print("Φόρτωση γνωστών προσώπων...")
known_encodings, known_names = load_known_faces(KNOWN_FACES_PATH)
print(f"Φορτώθηκαν {len(known_encodings)} γνωστά πρόσωπα από πολλαπλές εικόνες.")

# Επιλογή εισόδου
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

while video_capture.isOpened():
    ret, frame = video_capture.read()
    if not ret:
        print("Δεν είναι δυνατή η ανάγνωση από την πηγή.")
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    color_frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)

    face_locations = face_recognition.face_locations(gray_frame, model='cnn')
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        name = "Άγνωστος"

        if True in matches:
            match_index = matches.index(True)
            name = known_names[match_index]

        cv2.rectangle(color_frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(color_frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    cv2.imshow("Αναγνώριση Προσώπων", color_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
