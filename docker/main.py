import pytesseract
from PIL import Image, ImageDraw
import sys
import re

regex = ""
source_path = ""
dest_path = ""

if __name__ == "__main__":
    regex = sys.argv[1]
    source_path = sys.argv[2]
    dest_path = sys.argv[3]

print("Regex:", regex)
print("Source Path:", source_path)
print("Destination Path:", dest_path)

image = Image.open(source_path)
draw = ImageDraw.Draw(image)

data = pytesseract.image_to_data(image, output_type='dict')
print("TXT:", data['text'])

boxes = len(data['level'])
for i in range(boxes):
    if data['text'][i] != '':
        if re.search(regex, data['text'][i]) is not None:
            (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
            draw.rectangle([x, y, x+w, y+h], outline="black", fill="black")


image.save(dest_path)

