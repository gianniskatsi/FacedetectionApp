import face_recognition
import cv2
import numpy as np

# Φόρτωση γνωστών προσώπων και χαρακτηριστικών
known_face_encodings = []
known_face_names = []

# Φορτώστε εικόνες και ονόματα (παραδείγματα)
image_of_person1 = face_recognition.load_image_file("person1.jpg")
person1_encoding = face_recognition.face_encodings(image_of_person1)[0]
known_face_encodings.append(person1_encoding)
known_face_names.append("Person 1")

image_of_person2 = face_recognition.load_image_file("person2.jpg")
person2_encoding = face_recognition.face_encodings(image_of_person2)[0]
known_face_encodings.append(person2_encoding)
known_face_names.append("Person 2")

# Χρήση κάμερας
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # Μετατροπή σε μικρότερο μέγεθος για ταχύτητα
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]  # Μετατροπή BGR -> RGB

    # Εύρεση προσώπων και χαρακτηριστικών
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    # Σύγκριση προσώπων
    face_names = []
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        # Αν υπάρχει ταύτιση
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        face_names.append(name)

    # Εμφάνιση αποτελεσμάτων
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Επαναφορά μεγέθους
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Σχεδίαση πλαισίου
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        # Εμφάνιση ονόματος
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
        cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 1)

    # Μετατροπή σε ασπρόμαυρη εικόνα
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Video', gray_frame)

    # Τερματισμός με το πλήκτρο 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Απελευθέρωση πόρων
video_capture.release()
cv2.destroyAllWindows()
