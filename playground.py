# https://pypi.org/project/pytesseract/
import cv2
try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract


def show_langs():
    '''
    Esta weaita es un caprisho, ignore
    '''

    PATH = '/usr/local/Cellar/tesseract-lang/4.0.0/share/tessdata/langs.txt'
    with open(PATH, 'r') as file:
        print([line.strip('\n') for line in file.readlines()])


'''
print(pytesseract.image_to_string(Image.open(f'refranes/refranes-002.png'), lang='spa'))
print('\n==============\n')
print(pytesseract.image_to_string(Image.open(f'img/pag2.png'), lang='spa'))
'''


def read():
    for n in range(1, 101):
        with open('raws_bw/pag{:0>3d}.txt'.format(n), 'w') as pag:
            pag.write(pytesseract.image_to_string(Image.open('refranes_bw/refranes_bw-{:0>3d}.png'.format(n)), lang='spa'))

# print(pytesseract.image_to_string(Image.open('raws_bw/test.png'), lang='spa'))

def grayscale():
    for n in range(1,101):
        image = cv2.imread('refranes/refranes-{:0>3d}.png'.format(n))
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('refranes_bw/refranes_bw-{:0>3d}.png'.format(n), gray)

read()
