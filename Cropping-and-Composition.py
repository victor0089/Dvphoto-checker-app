pip install opencv-python
import cv2

def verify_photo(photo_path, required_face_percentage):
    try:
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

        # Assuming the first detected face
        x, y, w, h = faces[0]

        # Calculate the face size as a percentage of the image size
        img_height, img_width = photo.shape[:2]
        face_percentage = (w * h) / (img_width * img_height) * 100

        # Check if the face is centered and occupies the required percentage
        if abs(x + w / 2 - img_width / 2) < img_width * 0.1 and face_percentage >= required_face_percentage:
            return True  # Photo meets the requirements

        return False  # Photo does not meet the requirements

    except Exception as e:
        # Handle any exceptions, such as file not found or invalid image format
        return False

# Example usage
photo_path = "captured_photo.jpg"
required_face_percentage = 20  # Adjust as needed

result = verify_photo(photo_path, required_face_percentage)
if result:
    print("Photo meets DV Lottery requirements.")
else:
    print("Photo does not meet requirements.")
