pip install opencv-python
pip install dlib
import cv2
import dlib
import math

def calculate_face_orientation(shape):
    # Calculate the angle between the eyes and the horizontal axis
    eye_left = shape[36]
    eye_right = shape[45]
    dx = eye_right[0] - eye_left[0]
    dy = eye_right[1] - eye_left[1]
    angle = math.atan2(dy, dx) * 180.0 / math.pi

    return angle

def verify_photo(photo_path):
    # Load the captured photo
    photo = cv2.imread(photo_path)

    # Load the shape predictor model from dlib for facial landmarks detection
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    # Load the face detector model from dlib
    detector = dlib.get_frontal_face_detector()

    # Convert the image to grayscale for face detection
    grayscale = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = detector(grayscale)

    if len(faces) == 0:
        return False  # No face detected

    # Assuming the first detected face
    face = faces[0]

    # Detect facial landmarks
    shape = predictor(grayscale, face)

    # Calculate the head orientation angle
    angle = calculate_face_orientation(shape)

    # Define the allowed range for head orientation (e.g., -10 to 10 degrees for upright head)
    allowed_range = (-10, 10)

    if allowed_range[0] <= angle <= allowed_range[1]:
        return True  # Photo meets the requirements

    return False  # Photo does not meet the requirements

# Example usage
photo_path = "captured_photo.png"
result = verify_photo(photo_path)
if result:
    print("Photo meets DV Lottery requirements.")
else:
    print("Photo does not meet requirements.")
