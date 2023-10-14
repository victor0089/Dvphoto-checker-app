pip install dlib
pip install opencv-python

import dlib
import cv2
import math

def calculate_eye_distance(shape):
    # Define the indices of the left and right eyes in the shape
    left_eye_index = [36, 37, 38, 39, 40, 41]
    right_eye_index = [42, 43, 44, 45, 46, 47]

    # Calculate the distance between the centers of the left and right eyes
    left_eye_center = (sum([shape[i][0] for i in left_eye_index]) // 6, sum([shape[i][1] for i in left_eye_index]) // 6)
    right_eye_center = (sum([shape[i][0] for i in right_eye_index]) // 6, sum([shape[i][1] for i in right_eye_index]) // 6)

    distance = math.dist(left_eye_center, right_eye_center)

    return distance

def verify_photo(photo_path, required_eye_distance):
    try:
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

        # Calculate the distance between the eyes
        eye_distance = calculate_eye_distance(shape)

        # Check if the eye distance meets the required distance
        if abs(eye_distance - required_eye_distance) <= 5:  # A tolerance of 5 pixels
            return True  # Photo meets the requirements

        return False  # Photo does not meet the requirements

    except Exception as e:
        # Handle any exceptions, such as file not found or invalid image format
        return False

# Example usage
photo_path = "captured_photo.jpg"
required_eye_distance = 100  # Adjust as needed

result = verify_photo(photo_path, required_eye_distance)
if result:
    print("Photo meets DV Lottery requirements.")
else:
    print("Photo does not meet requirements.")
