import cv2
import numpy as np

def calculate_eye_distance(shape):
    # Calculate the distance between the centers of the left and right eyes
    left_eye = shape[36:42]
    right_eye = shape[42:48]

    left_eye_center = np.mean(left_eye, axis=0)
    right_eye_center = np.mean(right_eye, axis=0)

    distance = np.linalg.norm(left_eye_center - right_eye_center)

    return distance

def calculate_background_uniformity(photo_path):
    # Load the captured photo
    photo = cv2.imread(photo_path)

    # Convert the image to grayscale
    grayscale = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)

    # Calculate the standard deviation of pixel values in the grayscale image
    std_dev = np.std(grayscale)

    return std_dev

def provide_feedback(photo_path, required_resolution, required_eye_distance, uniformity_threshold):
    feedback = []

    # Check image resolution
    image = cv2.imread(photo_path)
    img_height, img_width = image.shape[:2]

    if img_width != required_resolution[0] or img_height != required_resolution[1]:
        feedback.append("Resolution does not meet the requirements.")

    # Load the shape predictor model from dlib for facial landmarks detection
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    # Load the face detector model from dlib
    detector = dlib.get_frontal_face_detector()

    # Convert the image to grayscale for face detection
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = detector(grayscale)

    if len(faces) == 0:
        feedback.append("No face detected.")

    else:
        # Assuming the first detected face
        face = faces[0]

        # Detect facial landmarks
        shape = predictor(grayscale, face)

        # Calculate the eye distance
        eye_distance = calculate_eye_distance(shape)

        # Check if the eye distance meets the required distance
        if abs(eye_distance - required_eye_distance) > 5:
            feedback.append("Eye distance does not meet the requirements.")

    # Calculate background uniformity
    std_dev = calculate_background_uniformity(photo_path)

    if std_dev > uniformity_threshold:
        feedback.append("Background is not uniform.")

    if not feedback:
        return "Photo meets DV Lottery requirements."
    else:
        return "Photo does not meet requirements. Reasons:\n" + "\n".join(feedback)

# Example usage
photo_path = "captured_photo.jpg"
required_resolution = (600, 600)
required_eye_distance = 100
uniformity_threshold = 10

feedback_message = provide_feedback(photo_path, required_resolution, required_eye_distance, uniformity_threshold)
print(feedback_message)
