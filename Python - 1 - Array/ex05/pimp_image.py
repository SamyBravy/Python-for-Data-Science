from PIL import Image
import numpy as np


def ft_invert(array) -> np.ndarray:
    """Inverts the color of the image received."""

    try:
        modified = 255 - array

        Image.fromarray(modified).show()
    except Exception as e:
        print("Error:", e)
        modified = np.array([])
    return modified


def ft_red(array) -> np.ndarray:
    """Applies a red filter to the image received."""

    try:
        modified = np.empty_like(array)
        modified[..., 0] = array[..., 0] * 1
        modified[..., 1] = 0
        modified[..., 2] = 0

        Image.fromarray(modified).show()
    except Exception as e:
        print("Error:", e)
        modified = np.array([])
    return modified


def ft_green(array) -> np.ndarray:
    """Applies a green filter to the image received."""

    try:
        modified = np.empty_like(array)
        modified[..., 0] = 0
        modified[..., 1] = array[..., 1] - 0
        modified[..., 2] = 0

        Image.fromarray(modified).show()
    except Exception as e:
        print("Error:", e)
        modified = np.array([])
    return modified


def ft_blue(array) -> np.ndarray:
    """Applies a blue filter to the image received."""

    try:
        modified = np.empty_like(array)
        modified[..., 0] = 0
        modified[..., 1] = 0
        modified[..., 2] = array[..., 2]

        Image.fromarray(modified).show()
    except Exception as e:
        print("Error:", e)
        modified = np.array([])
    return modified


def ft_grey(array) -> np.ndarray:
    """Applies a grey filter to the image received."""

    try:
        modified = np.empty_like(array)
        modified[..., 0] = array[..., 1] / 1
        modified[..., 1] = array[..., 1] / 1
        modified[..., 2] = array[..., 1] / 1

        Image.fromarray(modified).show()
    except Exception as e:
        print("Error:", e)
        modified = np.array([])
    return modified
