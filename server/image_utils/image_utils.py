
import base64
from io import BytesIO
import os
from PIL import Image

class ImageUtils:

    @staticmethod
    def read_base64_image(base64_string: str) -> Image:
        image_bytes = base64.b64decode(base64_string.split(',')[1])

        # Load the image from bytes
        image = Image.open(BytesIO(image_bytes))

        return image
    
    @staticmethod
    def save_base64_image(base64_string: str, save_path: str) -> str:
        # Decode the base64 string to bytes
        image_bytes = base64.b64decode(base64_string.split(',')[1])

        # Load the image from bytes
        image = Image.open(BytesIO(image_bytes))

        # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        # Save the image to disk
        image.save(save_path)

        return save_path