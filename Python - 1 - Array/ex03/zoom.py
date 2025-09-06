from load_image import ft_load
from PIL import Image
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

data = ft_load("animal.jpeg")
if data == []:
    exit(1)
print(data)

h, w, _ = data.shape
crop = data[h//13: 4 * h//6, 2 * w//5: 2 * w//5 + 4 * h//6 - h//13]
zoomed = ndimage.zoom(crop, (4, 4, 1))
img = Image.fromarray(zoomed.astype(np.uint8))

img = img.convert("L")
data = np.asarray(img)[..., np.newaxis]

print("New shape after slicing:", data.shape, "or", data.shape[:-1])
print(data)

plt.imshow(data.squeeze(), cmap='gray')
plt.show()
