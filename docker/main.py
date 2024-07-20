import matplotlib
##matplotlib.use('TkAgg')
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import pytesseract
from PIL import Image
import sys
import re

regex = ""
source_path = ""
dest_path = ""

if __name__ == "__main__":
    regex = sys.argv[1]
    source_path = sys.argv[2]
    dest_path = sys.argv[3]

# regex = "((?<!\d)\d{16}(?!\d)|(?<!\d[ _-])(?<!\d)\d{4}(?:[_ -]\d{4}){3}(?![_ -]?\d))|((?<!\d)\d{16}(?!\d)|(?<!\d[ _-])(?<!\d)\d{4}(?=([_ -]))(?:\1\d{4}){3}(?![_ -]?\d))|((?<!\d)\d{16}(?!\d)|(?<!\d[ _-])(?<!\d)\d{4}([_ -])\d{4}(?:\1\d{4}){2}(?![_ -]?\d))|((age|gender|Dulce|a))|(^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$)|(^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$)|(^\d+$)|(^\(?\d{3}\)?[- ]?\d{3}[- ]?\d{4}$)|(/(?:\(?\+\d{2}\)?\s*)?\d+(?:[ -]*\d+)*$/)|(\\(\\d{3}\\)\\s\\d{3}-\\d{4})"





image = Image.open(source_path)
np_image = np.array(image, dtype=np.uint8)

print(np_image.shape)

fig, ax = plt.subplots(1)
plt.axis('off')

data = pytesseract.image_to_data(image, output_type='dict')
print("TXT:", data['text'])

boxes = len(data['level'])
for i in range(boxes):
    if data['text'][i] != '':
        if re.search(regex, data['text'][i]) is not None:
            rect = patches.Rectangle((data['left'][i], data['top'][i]), data['width'][i], data['height'][i], linewidth=1,
                                     edgecolor='black', facecolor="black")
            ax.add_patch(rect)
        # print(data['left'][i], data['top'][i], data['width'][i], data['height'][i], data['text'][i])


plt.imshow(np_image)
# plt.show()

ax.plot()
fig.savefig(dest_path, bbox_inches='tight', pad_inches=0, dpi=400)
