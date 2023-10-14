pip install Pillow

from PIL import Image
import os

def verify_photo(photo_path, allowed_formats, max_file_size_kb):
    try:
        # Open the photo using Pillow
        image = Image.open(photo_path)

        # Check file format
        file_format = image.format
        if file_format not in allowed_formats:
            return False  # Photo format is not allowed

        # Check file size
        file_size_bytes = os.path.getsize(photo_path)
        max_file_size_bytes = max_file_size_kb * 1024  # Convert kilobytes to bytes
        if file_size_bytes > max_file_size_bytes:
            return False  # Photo size exceeds the allowed limit

        return True  # Photo meets the requirements

    except Exception as e:
        # Handle any exceptions, such as file not found or invalid image format
        return False

# Example usage
photo_path = "captured_photo.jpg"
allowed_formats = {"JPEG", "JPG"}  # Adjust as needed
max_file_size_kb = 240  # Adjust as needed

result = verify_photo(photo_path, allowed_formats, max_file_size_kb)
if result:
    print("Photo meets DV Lottery requirements.")
else:
    print("Photo does not meet requirements.")
