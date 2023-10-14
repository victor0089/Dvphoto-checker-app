import os

# Define a directory for storing photos
photo_storage_directory = "photo_storage"

def save_photo(user_id, photo_data):
    # Generate a unique file name for each user
    file_name = f"{user_id}_photo.jpg"

    # Construct the file path
    file_path = os.path.join(photo_storage_directory, file_name)

    # Ensure the storage directory exists
    os.makedirs(photo_storage_directory, exist_ok=True)

    # Save the photo data to the file
    with open(file_path, 'wb') as file:
        file.write(photo_data)

    # Return the file path for future reference
    return file_path

# Example usage
user_id = "user123"
photo_data = b"Binary photo data"

file_path = save_photo(user_id, photo_data)
print(f"Photo saved to: {file_path}")
