import face_recognition
import cv2

# Φόρτωση εικόνας ή καρέ από κάμερα
video_capture = cv2.VideoCapture(0)  # Χρήση κάμερας

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # Εύρεση τοποθεσιών προσώπων
    face_locations = face_recognition.face_locations(frame)
    
    # Εύρεση χαρακτηριστικών προσώπων (encodings)
    face_encodings = face_recognition.face_encodings(frame, face_locations)
    
    for face_encoding, face_location in zip(face_encodings, face_locations):
        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    # Εμφάνιση καρέ
    cv2.imshow('Video', frame)

    # Τερματισμός με το πλήκτρο 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Απελευθέρωση πόρων
video_capture.release()
cv2.destroyAllWindows()
