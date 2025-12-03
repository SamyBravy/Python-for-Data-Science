from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def zoom(data):
    """
    Zooms into a specific region of the image and returns the zoomed image.
    """

    h, w, _ = data.shape
    crop = data[h//13: 4 * h//6, 2 * w//5: 2 * w//5 + 4 * h//6 - h//13]
    img = Image.fromarray(crop)
    return img


def transpose(data):
    """
    Transposes the image by swapping its rows and columns.
    """

    h, w = data.shape
    transposed = np.empty((w, h), dtype=data.dtype)
    for i in range(h):
        for j in range(w):
            transposed[j, i] = data[i, j]
    return transposed


def main():
    """Main function to load, process, and display the image."""

    data = ft_load("animal.jpeg")
    if data.size == 0:
        exit(1)

    img = zoom(data)

    img = img.convert("L")
    data = np.asarray(img)[..., np.newaxis]

    print("The shape of image is:", data.shape, "or", data.shape[:-1])
    print(data)

    data = transpose(data.squeeze())

    print("New shape after Transpose:", data.shape[:-1])
    print(data)

    plt.imshow(data.squeeze(), cmap='gray')
    plt.show()


if __name__ == "__main__":
    main()
