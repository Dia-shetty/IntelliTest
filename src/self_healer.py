import cv2
import imagehash
from PIL import Image

def heal_locator(old_image_path, new_image_path):
    """
    Compares old and new screenshots to detect UI changes and suggest new locators.
    """
    old_hash = imagehash.average_hash(Image.open(old_image_path))
    new_hash = imagehash.average_hash(Image.open(new_image_path))
    diff = old_hash - new_hash
    if diff > 5:
        print(f"⚠️ UI changed! Hash difference = {diff}. Need to update locator.")
        return False
    else:
        print("✅ Locator still valid.")
        return True

if __name__ == "__main__":
    heal_locator("old_button.png", "new_button.png")
