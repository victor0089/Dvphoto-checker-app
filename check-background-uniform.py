# pip install opencv-python #

import cv2
import numpy as np

def verify_photo(photo_path):
    # Load the captured hhhh photo
    photo = cv2.imread(photo_path)

    # Convert the image to grayscale for background analysis
    grayscale = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)

    # Calculate the standard deviation of pixel values in the grayscale image
    std_dev = np.std(grayscale)

    # Define a threshold for background uniformity
    uniformity_threshold = 10  # Adjust as needed

    # Check if the standard deviation is below the threshold, indicating a uniform background
    if std_dev < uniformity_threshold:
        return True  # Photo meets the requirements

    return False  # Photo does not meet the requirements

# Example usage
photo_path = "captured_photo.png"
result = verify_photo(photo_path)
if result:
    print("Photo meets DV Lottery requirements.")
else:
    print("Photo does not meet requirements.")
