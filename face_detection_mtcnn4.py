import cv2
import face_recognition
import os

# Έλεγχος για γνωστά πρόσωπα
KNOWN_FACES_PATH = "C:\\Project\\Known_faces"
known_encodings = []
known_names = []

if not os.path.exists(KNOWN_FACES_PATH):
    print("Ο φάκελος γνωστών προσώπων δεν βρέθηκε.")
    exit()

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

# Επιλογή εισόδου
choice = input("Πατήστε 1 για κάμερα ή 2 για αποθηκευμένο βίντεο: ")
if choice == "1":
    video_source = 0
elif choice == "2":
    video_source = "C:/Project/video/export_1713300134091.MP4".strip()
    if not os.path.exists(video_source):
        print(f"Το αρχείο βίντεο δεν βρέθηκε στο μονοπάτι: {video_source}")
        exit()
else:
    print("Μη έγκυρη επιλογή.")
    exit()

# Εκκίνηση βίντεο
video_capture = cv2.VideoCapture(video_source)

while video_capture.isOpened():
    ret, frame = video_capture.read()
    if not ret:
        print("Δεν είναι δυνατή η ανάγνωση από την πηγή.")
        break

    # Μετατροπή καρέ σε ασπρόμαυρο για ανίχνευση
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Ανίχνευση προσώπων
    face_locations = face_recognition.face_locations(gray_frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Προετοιμασία για σχεδιασμό
    color_frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)

    for face_location, face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        name = "Άγνωστος"

        if True in matches:
            match_index = matches.index(True)
            name = known_names[match_index]

        top, right, bottom, left = face_location

        # Κόκκινο περίγραμμα
        cv2.rectangle(color_frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Διαφανές κόκκινο πλαίσιο
        overlay = color_frame.copy()
        cv2.rectangle(overlay, (left, top), (right, bottom), (0, 0, 255), -1)
        alpha = 0.3
        color_frame = cv2.addWeighted(overlay, alpha, color_frame, 1 - alpha, 0)

        # Εμφάνιση ονόματος
        cv2.putText(
            color_frame,
            name,
            (left, top - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 0, 255),
            2
        )

    # Εμφάνιση βίντεο
    cv2.imshow("Αναγνώριση Προσώπων", color_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Καθαρισμός
video_capture.release()
cv2.destroyAllWindows()
