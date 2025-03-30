import cv2
import face_recognition
import os
import pandas as pd
from datetime import datetime
import re
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
import numpy as np


known_faces_dir = 'known_faces'
attendance_file = 'attendance.xlsx'


if not os.path.exists(known_faces_dir):
    os.makedirs(known_faces_dir)

known_face_encodings = []
known_face_names = []

def load_known_faces():
    global known_face_encodings, known_face_names
    known_face_encodings = []
    known_face_names = []
    
    for filename in os.listdir(known_faces_dir):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image_path = os.path.join(known_faces_dir, filename)
            image = face_recognition.load_image_file(image_path)
            encoding = face_recognition.face_encodings(image)
            if encoding:
                known_face_encodings.append(encoding[0])
                known_face_names.append(os.path.splitext(filename)[0])

load_known_faces()

def extract_name_and_enrollment(outlook_id):
    if "cseu" in outlook_id:
        match = re.search(r'cseu(\d+)', outlook_id)
        if match:
            enrollment_number = match.group(1)
            if len(enrollment_number) >= 4:
                return None, enrollment_number
    else:
        name_match = re.match(r'([^@]+)@', outlook_id)
        if name_match:
            name = name_match.group(1)
            return name, None
    return None, None

def log_attendance(name, enrollment_number):
    current_time = datetime.now()
    attendance_data = {
        "Name": name if name else "Unknown",
        "Enrollment Number": enrollment_number if enrollment_number else "Unknown",
        "Date": current_time.date(),
        "Time": current_time.time()
    }
    attendance_df = pd.DataFrame([attendance_data])
    
    if os.path.exists(attendance_file):
        with pd.ExcelWriter(attendance_file, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
            attendance_df.to_excel(writer, index=False, header=False, startrow=writer.sheets['Sheet1'].max_row, sheet_name='Sheet1')
    else:
        attendance_df.to_excel(attendance_file, index=False)

class CustomDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(CustomDialog, self).__init__(parent)
        self.setWindowTitle('Bennett University - New User Detected')
        self.setFixedSize(400, 200)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)
        
        
        self.setStyleSheet("background-color: #f2f2f2;")
        
        layout = QtWidgets.QVBoxLayout(self)
        
        title_label = QtWidgets.QLabel("Welcome to Bennett University!")
        title_label.setAlignment(QtCore.Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 20px; font-weight: bold; color: #2E86C1;")
        layout.addWidget(title_label)

        self.outlook_input = QtWidgets.QLineEdit(self)
        self.outlook_input.setPlaceholderText("Enter your Outlook ID...")
        self.outlook_input.setStyleSheet("padding: 10px; border: 1px solid #ccc; border-radius: 5px;")
        layout.addWidget(self.outlook_input)

        button_layout = QtWidgets.QHBoxLayout()
        self.submit_button = QtWidgets.QPushButton("Submit")
        self.submit_button.setStyleSheet("background-color: #2E86C1; color: white; padding: 10px; border: none; border-radius: 5px;")
        self.cancel_button = QtWidgets.QPushButton("Cancel")
        self.cancel_button.setStyleSheet("background-color: #e74c3c; color: white; padding: 10px; border: none; border-radius: 5px;")
        
        button_layout.addWidget(self.submit_button)
        button_layout.addWidget(self.cancel_button)
        
        layout.addLayout(button_layout)
        
        
        self.submit_button.clicked.connect(self.submit)
        self.cancel_button.clicked.connect(self.reject)

    def submit(self):
        outlook_id = self.outlook_input.text()
        if outlook_id:
            self.accept()  
        else:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Please enter a valid Outlook ID.")

    def get_outlook_id(self):
        return self.outlook_input.text()

class AttendanceApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.video_capture = cv2.VideoCapture(0)
        self.video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.logged_users = set()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.process_frame)
        self.timer.start(100)

        self.outlook_id_timer = QtCore.QTimer()
        self.outlook_id_timer.setSingleShot(True)
        self.outlook_id_timer.timeout.connect(self.ask_outlook_id)
        self.current_frame = None  
        self.is_new_user = False  
        self.is_user_identified = False  

    def initUI(self):
        self.setWindowTitle('Face Attendance System')
        self.setGeometry(100, 100, 800, 600)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(10, 10, 640, 480)
        self.button = QtWidgets.QPushButton('Quit', self)
        self.button.setGeometry(10, 500, 100, 30)
        self.button.clicked.connect(self.close)

    def process_frame(self):
        ret, frame = self.video_capture.read()
        if not ret:
            print("Failed to capture video.")
            return
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame, model="hog")
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        if face_locations and face_encodings:
            for face_encoding, face_location in zip(face_encodings, face_locations):
                name = "Unknown"
                if known_face_encodings:
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.5)
                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)

                    best_match_index = np.argmin(face_distances) if face_distances.size > 0 else None

                    if matches[best_match_index] and face_distances[best_match_index] < 0.4:
                        name = known_face_names[best_match_index]
                        if name not in self.logged_users:
                            log_attendance(name, "")
                            self.logged_users.add(name)
                        cv2.putText(frame, "Attendance Marked", (face_location[3], face_location[2] + 30),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                        color = (0, 255, 0)  
                        self.is_new_user = False  
                        self.is_user_identified = True  
                    else:
                        
                        if not self.is_new_user:
                            self.current_frame = frame.copy()  
                            self.outlook_id_timer.start(4000)  
                            self.is_new_user = True
                            self.is_user_identified = False  
                        color = (0, 0, 255)  
                else:
                    color = (0, 0, 255)  

                (top, right, bottom, left) = face_location
                cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
                cv2.putText(frame, name if name != "Unknown" else "New User", (left, bottom + 15),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        height, width, channel = frame.shape
        bytes_per_line = 3 * width
        q_image = QtGui.QImage(frame.data, width, height, bytes_per_line, QtGui.QImage.Format_BGR888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(q_image))

    def ask_outlook_id(self):
        if self.is_new_user:  
            self.show_outlook_dialog()  

    def show_outlook_dialog(self):
        dialog = CustomDialog(self)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            outlook_id = dialog.get_outlook_id()
            name, enrollment_number = extract_name_and_enrollment(outlook_id)

            if (name or enrollment_number):
                new_face_filename = f"{name if name else enrollment_number}.jpg"
                new_face_image_path = os.path.join(known_faces_dir, new_face_filename)
                cv2.imwrite(new_face_image_path, self.current_frame)

                load_known_faces()

                face_encodings = face_recognition.face_encodings(self.current_frame)
                if face_encodings:
                    new_face_encoding = face_encodings[0]
                    known_face_encodings.append(new_face_encoding)
                    known_face_names.append(name if name else enrollment_number)

                    log_attendance(name, enrollment_number)
                    if name:
                        self.logged_users.add(name)
                else:
                    print("No face encoding found in the captured image after saving.")
            else:
                print("Invalid Outlook ID format. Showing dialog again in 3 seconds.")
                self.outlook_id_timer.start(3000)  
        else:
            print("Dialog canceled. Showing dialog again in 3 seconds.")
            self.outlook_id_timer.start(3000) 

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    attendance_app = AttendanceApp()
    attendance_app.show()
    sys.exit(app.exec_())
print("hiiiiii")
