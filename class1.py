from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.popup import Popup
#  Create the App Class #
class DVPhotoCheckerApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.camera = Camera(play=True)
        self.capture_button = Button(text="Capture Photo")
        self.capture_button.bind(on_press=self.capture_photo)
        layout.add_widget(self.camera)
        layout.add_widget(self.capture_button)
        return layout

    def capture_photo(self, instance):
        self.camera.export_to_png("captured_photo.png")
        photo_verification_result = self.verify_photo("captured_photo.png")

        if photo_verification_result:
            popup = Popup(title='Photo Verified', content=Label(text='Your photo meets DV Lottery requirements.'),
                          auto_dismiss=True, size_hint=(None, None), size=(400, 200))
        else:
            popup = Popup(title='Photo Not Verified', content=Label(text='Your photo does not meet requirements.'),
                          auto_dismiss=True, size_hint=(None, None), size=(400, 200))

        popup.open()

    def verify_photo(self, photo_path):
        # Implement your photo verification algorithm here
        # Check size, resolution, background color, head size, etc.
        # Return True if the photo meets the requirements, otherwise return False
        pass

# verify_photo #
import cv2
import numpy as np

def verify_photo(photo_path):
    # Load the captured photo
    photo = cv2.imread(photo_path)
    
    # Check photo size (e.g., must be 600x600 pixels)
    required_size = (600, 600)
    if photo.shape[:2] != required_size:
        return False

    # Convert the image to grayscale for further processing
    grayscale = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
    
    # Implement additional checks for head position and background color
    # You may need to fine-tune these parameters according to DV Lottery requirements
    # Here's a simple example:
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(grayscale, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))
    
    if len(faces) == 0:
        return False  # No face detected

    # Check background color (e.g., white)
    average_color = np.mean(photo, axis=(0, 1))
    if not is_white_background(average_color):
        return False

    return True  # Photo meets the basic requirements

def is_white_background(color):
    # Define a threshold for considering the background as white
    threshold = 200
    return all(c >= threshold for c in color)

# Example usage
photo_path = "captured_photo.png"
result = verify_photo(photo_path)
if result:
    print("Photo meets DV Lottery requirements.")
else:
    print("Photo does not meet requirements.")
# 
import cv2

def verify_photo(photo_path):
    # Load the captured photo
    photo = cv2.imread(photo_path)

    # Convert the image to grayscale for face detection
    grayscale = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)

    # Load the face cascade classifier for detecting faces
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(grayscale, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))

    if len(faces) == 0:
        return False  # No face detected

    # Check if the first detected face is centered and occupies a specific percentage of the image
    x, y, w, h = faces[0]  # Assuming the first detected face
    img_height, img_width = photo.shape[:2]

    # Define the acceptable range for centering
    center_x_range = (img_width * 0.4, img_width * 0.6)
    center_y_range = (img_height * 0.4, img_height * 0.6)

    # Define the required face size as a percentage of the image size
    required_face_size_percentage = 20  # Adjust as needed

    # Check if the face is centered and occupies the required percentage
    if center_x_range[0] < (x + w / 2) < center_x_range[1] and center_y_range[0] < (y + h / 2) < center_y_range[1]:
        # Calculate the face size as a percentage of the image size
        face_percentage = (w * h) / (img_width * img_height) * 100

        if face_percentage >= required_face_size_percentage:
            return True  # Photo meets the requirements

    return False  # Photo does not meet the requirements

# Example usage
photo_path = "captured_photo.png"
result = verify_photo(photo_path)
if result:
    print("Photo meets DV Lottery requirements.")
else:
    print("Photo does not meet requirements.")

