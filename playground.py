# https://pypi.org/project/pytesseract/
import cv2
try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract
from pytesseract import Output
import random

def show_langs():
    '''
    Esta weaita es un caprisho, ignore
    '''

    PATH = '/usr/local/Cellar/tesseract-lang/4.0.0/share/tessdata/langs.txt'
    with open(PATH, 'r') as file:
        print([line.strip('\n') for line in file.readlines()])


def read():
    for n in range(1, 101):
        with open('raws_bw/pag{:0>3d}.txt'.format(n), 'w') as pag:
            pag.write(pytesseract.image_to_string(Image.open('refranes_bw/refranes_bw-{:0>3d}.png'.format(n)), lang='spa'))


def grayscale():
    for n in range(1,101):
        image = cv2.imread('refranes/refranes-{:0>3d}.png'.format(n))
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('refranes_bw/refranes_bw-{:0>3d}.png'.format(n), gray)

# Tests ======================================================================

IMG1 = 'refranes_bw/refranes_bw-052.png'
IMG = 'test4.png'
img = cv2.imread(IMG1)

d = pytesseract.image_to_data(img, output_type=Output.DICT)
n_boxes = len(d['level'])
edges = [0, 0, 0, 0]

for i in range(1, n_boxes):
    if d['text'][i] == " ":
        continue
    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
    if d['text'][i] == "" and 50 <= d["height"][i]:
        color = (0, 0, 255)
        edges = [x, y, x+w, y+h]
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)

    # elif all([x >= edges[0], y >= edges[1], x+w <= edges[2], y+h <= edges[3]]):
        #color = (255, 0, 0)
        #cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)

    print("top: {0} || ({2}, {3}) \"{1}\"".format(d['top'][i], d['text'][i], d['width'][i], d['height'][i]))

cv2.imshow('img', img)
cv2.waitKey(0)
