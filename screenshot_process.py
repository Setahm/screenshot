import pyautogui
from PIL import Image
import zipfile
import os

screenshot = pyautogui.screenshot()

bw_image = screenshot.convert("L")

flipped_image = bw_image.transpose(Image.FLIP_LEFT_RIGHT)

image_path = r" "     //add your image path to Save in Desktop

os.makedirs(os.path.dirname(image_path), exist_ok=True)

zip_path = r""      //add your image path what need to compressed it.
with zipfile.ZipFile(zip_path, "w") as zipf:
    zipf.write(image_path, arcname="screenshot_bw_flipped.png")

print("Screenshot processed, saved, and zipped in Pictures\\Screenshots!")
