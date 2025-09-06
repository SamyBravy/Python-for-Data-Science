from numpy import asarray
from PIL import Image


def is_valid_image_pillow(file_name):
    """Check if the file is a valid image."""
    try:
        with Image.open(file_name) as img:
            img.verify()    # not corrupted
            return True
    except (IOError, SyntaxError):
        return False


def ft_load(path: str) -> list:
    """
    Loads an image from the specified path
    and returns it as a 3D list of RGB values.
    """
    if not isinstance(path, str):
        print("Error: path must be a string")
        return []
    if not is_valid_image_pillow(path):
        print("Error: File not found or invalid image format")
        return []
    with Image.open(path) as img:
        array_img = asarray(img)
        print("The shape of image is:", array_img.shape)

    return array_img
