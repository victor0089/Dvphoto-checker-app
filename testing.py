import os

def test_verification_algorithm(verification_function, test_photos_dir):
    passed = 0
    failed = 0

    for photo_filename in os.listdir(test_photos_dir):
        photo_path = os.path.join(test_photos_dir, photo_filename)
        if verification_function(photo_path):
            print(f"Photo {photo_filename} PASSED verification.")
            passed += 1
        else:
            print(f"Photo {photo_filename} FAILED verification.")
            failed += 1

    print(f"Verification testing complete.")
    print(f"Total photos tested: {passed + failed}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")

# Example usage
def verify_photo(photo_path):
    # Your verification algorithm here, e.g., using the `provide_feedback` function

test_photos_dir = "test_photos"  # Directory containing test photos

test_verification_algorithm(verify_photo, test_photos_dir)
