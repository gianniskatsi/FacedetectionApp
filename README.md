2.	Εγκατάσταση των Εξαρτήσεων
2.1 Python
Η Python είναι απαραίτητη για την υλοποίηση του συστήματος.
Ενέργειες:
1.	Κατεβάστε την Python 3.11.9 από την επίσημη ιστοσελίδα: https://www.python.org/downloads/.
2.	Κατά την εγκατάσταση, ενεργοποιήστε την επιλογή "Add Python to PATH".
3.	Ελέγξτε την εγκατάσταση με την εντολή:
python –version

Αναμενόμενο αποτέλεσμα: Εμφανίζεται η έκδοση της Python, π.χ., Python 3.11.9
4.	Σε περίπτωση που δεν εμφανίζεται το παραπάνω μήνυμα  πληκτρολογήστε στο Power shell:
C:\Users\xxx\AppData\Local\Programs\Python\Python311\python.exe –version

Αναμενόμενο αποτέλεσμα: Να εμφανιστεί η έκδοση της Python,  Python 3.11.9 , τότε το πρόβλημα αφορά τη ρύθμιση του PATH.
5.	 Διαχείριση Μεταβλητών Περιβάλλοντος
5..1.	Πατήστε Win + S και αναζητήστε Environment Variables.
5..2.	Κάντε κλικ στο Edit the system environment variables.
5..3.	Στο παράθυρο System Properties, πατήστε Environment Variables.
5..4.	Στη λίστα System variables, βρείτε τη μεταβλητή Path και επιλέξτε Edit.
5..5.	Βεβαιωθείτε ότι οι παρακάτω διαδρομές υπάρχουν στη λίστα:
5..5.1.	C:\Users\xxx\AppData\Local\Programs\Python\Python311
5..5.2.	C:\Users\xxx\AppData\Local\Programs\Python\Python311\Scripts
6.	Έλεγχος στο PATH
Εκτελέστε την εντολή στο Power Shell :
 $env:Path -split ";"

Αναμενόμενο αποτέλεσμα: Βεβαιωθείτε ότι οι παραπάνω διαδρομές εμφανίζονται στο αποτέλεσμα.
2.2 pip
Το pip είναι ο διαχειριστής πακέτων της Python που επιτρέπει την εγκατάσταση βιβλιοθηκών. To pip επι της ουσίας είναι το εργαλείο που σου επιτρέπει να εγκαταστήσεις βιβλιοθήκες που επεκτείνουν τη λειτουργικότητα της Python. Χωρίς το pip, η διαχείριση εξωτερικών βιβλιοθηκών θα ήταν δύσκολη.
Ενέργειες:
1.	Επισκεφτείτε το σύνδεσμο https://bootstrap.pypa.io/get-pip.py
2.	Θα σας ανοίξει ένα κείμενο το οποίο πρέπει να το αντιγράψετε 
3.	Ανοίξτε έναν επεξεργαστή κειμένου (Notepad)
4.	Επικολλήστε το περιεχόμενο
5.	Αποθηκεύστε το αρχείο ως εξής
•	Επιλέξτε File > Save As.
•	Δώστε όνομα: get-pip.py.
•	Επιλέξτε τη θέση αποθήκευσης, C:\Project.
•	Αλλάξτε το Save as type σε All Files και αποθηκεύστε με κατάληξη .py
6.	Ελέγξτε αν το pip είναι εγκατεστημένο:
	pip --version
Αναμενόμενο αποτέλεσμα: Εμφανίζεται η έκδοση του pip,  pip 24.3.1 from /usr/local/lib/python3.11/site-packages.
7.	Ελέγξτε που είναι εγκατεστημένο το pip με την εντολή στο Power Shell:
•	C:\WINDOWS\system32> py -m ensurepip –upgrade
•	C:\WINDOWS\system32> py -m pip –version (ενναλακτικά)
Αναμενόμενο αποτέλεσμα: Τη θέση και την εκδοση του PIP
8.	Εγκαταστήστε τις απαραίτητες βιβλιοθήκες με την παρακάτω εντολή στο Power Shell:
PS C:\Project> py -m pip install face_recognition
Αναμενόμενο αποτέλεσμα: Μηνύματα επιτυχούς εγκατάστασης των βιβλιοθηκών.
2.3 CMake
Το CMake χρησιμοποιείται για τη διαμόρφωση και μεταγλώττιση λογισμικού.
Ενέργειες:
1.	Εγκαταστήστε το CMake:
pip install cmake
Αναμενόμενο αποτέλεσμα: Μήνυμα επιτυχούς εγκατάστασης, π.χ., Successfully installed cmake-3.31.2.
2.	Ελέγξτε την εγκατάσταση:
cmake --version
Αναμενόμενο αποτέλεσμα: Εμφανίζεται η έκδοση του CMake, π.χ., cmake version 3.31.2.
2.4 Microsoft Visual Studio Build Tools
Το Microsoft Visual Studio είναι απαραίτητο για τη μεταγλώττιση του dlib.
Ενέργειες:
1.	Κατεβάστε το από την επίσημη ιστοσελίδα της Microsoft: https://visualstudio.microsoft.com/downloads/?q=build+tools.
2.	Κατά την εγκατάσταση (Modify) ελέγξτε να:
2.1.	Έχετε επιλέξει Desktop development with C++
2.1.	Βεβαιώσου ότι έχεις επιλέξει τα MSVC Compiler και Windows 10 SDK
2.1.	Επίλεξε το εργαλείο CMake
2.1.	Επανεκκίνησε τον υπολογιστή σου
3.	Ελέγξτε την εγκατάσταση με την εντολή στο Power shell:
cl
Αναμενόμενο αποτέλεσμα: Εμφανίζεται το μήνυμα Microsoft (R) C/C++ Optimizing Compiler.
4.	Σε περίπτωση που δεν εμφανίσει το παραπάνω μήνυμα και εμφανίσει το παρακάτω:
C:\WINDOWS\system32> cl
cl : The term 'cl' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again. 
At line:1 char:1
+ cl
+ ~~
    + CategoryInfo:ObjectNotFound: (cl:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

Το μήνυμα αυτό δείχνει ότι η εντολή cl δεν αναγνωρίζεται και υπάρχει πιθανότητα η διαδρομή (PATH) για το Visual Studio Compiler να μην έχει ρυθμιστεί σωστά στο περιβάλλον σας. Εκτελέστε τα παρακάτω βήματα ώστε να φτάσετε στο παραπάνω αναμενόμενο αποτέλεσμα. 
Άνοιγμα του Developer Command Prompt:
a)	Πατήστε το κουμπί Start (Έναρξη).
b)	Πληκτρολογήστε και ανοίξτε ως διαχειριστής : Developer Command Prompt for Visual Studio 2022
c)	Αφού ανοίξετε το Developer Command Prompt, πληκτρολογήστε: cl
d)	Αναμενόμενο Αποτέλεσμα: Εμφανίζεται ένα μήνυμα παρόμοιο με το παρακάτω.
Microsoft (R) C/C++ Optimizing Compiler Version 19.42.34436 for x86
Copyright (C) Microsoft Corporation.  All rights reserved.
usage: cl [ option... ] filename... [ /link linkoption... ]
2.5 Εγκατάσταση OpenCV
Το OpenCV χρησιμοποιείται για την επεξεργασία εικόνων και βίντεο.
Ενέργειες:
1.	Εγκαταστήστε το OpenCV πληκτρολογώντας στο Power Shell:
pip install opencv-python
Αναμενόμενο αποτέλεσμα: Μήνυμα επιτυχούς εγκατάστασης.
2.	Επιβεβαιώστε την εγκατάσταση αφού ανοίξουμε περιβάλλον Python:
>>>import cv2
>>>print(cv2.__version__)
Αναμενόμενο αποτέλεσμα: Εμφανίζεται η έκδοση του OpenCV, π.χ., 4.5.3.
2.6 Εγκατάσταση SciPy
Το SciPy χρησιμοποιείται για υποστήριξη υπολογισμών και στατιστικής ανάλυσης.
Ενέργειες:
1.	Εγκαταστήστε το SciPy:
pip install scipy
Αναμενόμενο αποτέλεσμα: Μήνυμα επιτυχούς εγκατάστασης.
3.	Επιβεβαιώστε την εγκατάσταση αφού ανοίξουμε περιβάλλον Python:
>>>import scipy
>>>print(scipy.__version__)
Αναμενόμενο αποτέλεσμα: Εμφανίζεται η έκδοση του SciPy, π.χ., 1.9.1

2.7 dlib
Η βιβλιοθήκη dlib χρησιμοποιείται για αναγνώριση και ανίχνευση προσώπων.
Ενέργειες:
1.	Εγκαταστήστε το dlib:
pip install dlib --no-binary dlib
Αναμενόμενο αποτέλεσμα: Μηνύματα που δείχνουν την επιτυχή μεταγλώττιση και εγκατάσταση.
2.8 Κατεβάστε τα προ-εκπαιδευμένα μοντέλα 
1.	shape_predictor_68_face_landmarks.dat
   - Χρησιμοποιείται για την ανίχνευση χαρακτηριστικών προσώπου.
   - Από τον ιστότοπο: http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
2.	dlib_face_recognition_resnet_model_v1.dat
  - Χρησιμοποιείται για την αναγνώριση προσώπων.
  - Από τον ιστότοπο: http://dlib.net/files/dlib_face_recognition_resnet_model_v1.dat.bz2
3.	Τοποθετήστε τα αρχεία στον φάκελο models του project  με την μορφή C:\Project\models και αποσιμπιέστετα.

2.9 Δημιουργία φακέλου known_faces  όπου περιέχει φακέλους με εικόνες προσώπων για αναγνώριση με την εξής δομή:
1.	Φάκελος known_faces

C:/Project/known_faces/
     ├── Person1/
     │   ├── image1.jpg
     │   ├── image2.jpg
     ├── Person2/
     │   ├── image1.jpg
     │   ├── image2.jpg

2.	 Βίντεο
 Το πρόγραμμα δέχεται βίντεο από τον φάκελο:
     C:/Project/video/export_1713300134091.MP4

3.	Επιβεβαιώστε τη δομή φακέλου:
Ο φάκελος C:/Project/ στον νέο υπολογιστή πρέπει να έχει την παρακάτω δομή:

C:/Project/
├── models/
│   ├── shape_predictor_68_face_landmarks.dat
│   ├── dlib_face_recognition_resnet_model_v1.dat
├── known_faces/
│   ├── Person1/
│   │   ├── image1.jpg
│   │   ├── image2.jpg
│   ├── Person2/
│       ├── image1.jpg
│       ├── image2.jpg
├── video/
│   ├── export_1713300134091.MP4
├── face_detection_bw.py

3.	Έλεγχος Εγκατάστασης
Αφού ολοκληρώσετε τις εγκαταστάσεις, πρέπει να επαληθεύσετε ότι όλα λειτουργούν σωστά.
3.1.	Έλεγχος Python
Ελέγξτε αν το pip είναι εγκατεστημένο με την εντολή:
python –version

Αναμενόμενο αποτέλεσμα: Εμφανίζεται η έκδοση της Python, π.χ., Python 3.11.9.
3.2.	Έλεγχος pip
Ελέγξτε αν το pip είναι εγκατεστημένο με την εντολή: 
pip –version

Αναμενόμενο αποτέλεσμα: Εμφανίζεται η έκδοση του pip 
3.3.	 Έλεγχος CMake
Ελέγξτε εάν το CMake είναι εγκατεστημένο με την εντολή: 
cmake –version

Αναμενόμενο αποτέλεσμα: Εμφανίζεται η έκδοση του CMake
3.4.	Έλεγχος Microsoft Visual Studio
Ελέγξτε εάν το Microsoft Visual Studio είναι εγκατεστημένο με την εντολή: 
Cl

Αναμενόμενο αποτέλεσμα: Εμφανίζεται το μήνυμα Microsoft (R) C/C++ Optimizing Compiler.
3.5.	Έλεγχος OpenCV
Ελέγξτε εάν το Open CV είναι εγκατεστημένο με την εντολή στο Power Shell:
Python και μετά το μήνυμα
Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
Τις παρακάτω εντολές:

import cv2
print(cv2.__version__)

Αναμενόμενο αποτέλεσμα: Εμφανίζεται η έκδοση του OpenCV, π.χ., 4.10.0.
3.6.	Έλεγχος SciPy
Ελέγξτε εάν το SciPy είναι εγκατεστημένο με την εντολή στο Power Shell:
Python και μετά το μήνυμα
Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
Τις παρακάτω εντολές:

import scipy
print(scipy.__version__)
Αναμενόμενο αποτέλεσμα: Εμφανίζεται η έκδοση του SciPy, π.χ., 1.14.1
3.7.	Έλεγχος dlib
Ελέγξτε αν το dlib είναι εγκατεστημένο με την εντολή στο Power Shell:
Python και μετά το μήνυμα
Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
Τις παρακάτω εντολές:
>>>import dlib print
>>>(dlib.__version__) 
>>>print(dlib.DLIB_USE_CUDA)
Αναμενόμενο αποτέλεσμα: Εμφάνιση της έκδοσης του DLIP 19.24.6 και True αν υποστηρίζεται η GPU για το DLIP, διαφορετικά False.
3.8.	Έλεγχος για τη βιβλιοθήκη Face Recognition
Ελέγξτε αν η βιβλιοθήκη Face Recognition είναι εγκατεστημένο με την εντολή στο Power Shell:
Python και μετά το μήνυμα
Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
Τις παρακάτω εντολές:
import face_recognition 
print(face_recognition.__version__)
Αναμενόμενο αποτέλεσμα: Εμφάνιση την έκδοση της βιβλιοθήκης, 1.2.3
