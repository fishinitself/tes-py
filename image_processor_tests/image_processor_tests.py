import sys
import numpy as np
from PIL import Image

#   python3 image_processor_tests.py img1.png img.png 0 0 0

try:
    sample_img_name = sys.argv[1]
    test_img_name = sys.argv[2]
    r = int(sys.argv[3])
    g = int(sys.argv[4])
    b = int(sys.argv[5])
except:
    print("error, wrong args")
    exit()

def load_image(img):
    img.load()
    data = np.asarray(img, dtype="int32")
    return data

def get_coords(img):
    indices = np.where(np.all(img == np.array([r, g, b, 255]), axis=-1))
    coords = set(zip(indices[0], indices[1]))
    return list(coords)

sample_img = load_image(Image.open(sample_img_name))
test_img = load_image(Image.open(test_img_name).resize((sample_img.shape[1], sample_img.shape[0])))

num_sample = get_coords(sample_img)
num_test = get_coords(test_img)

print(len(num_sample))
print(len(num_test))
print(len(set(num_sample) & set(num_test)))

perc = len(set(num_sample) & set(num_test)) / len(num_sample) * 100

print(str(perc))

