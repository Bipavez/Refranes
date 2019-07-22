# https://pypi.org/project/pytesseract/

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


# print(pytesseract.image_to_data(Image.open('test6.png'), lang='spa'))
print(pytesseract.image_to_string(Image.open(f'img/pag9.1.png'), lang='spa'))

'''
for n in range(4,11):
    with open(f'pag{n}.txt','w') as pag:
        pag.write(pytesseract.image_to_string(Image.open(f'img/pag{n}.png'), lang='spa'))
'''
'''
Esto es una weaita que toy testeando xd


img = Image.open('testx.png')
print(pytesseract.image_to_string(img), '\n----\n')
new_size = tuple(2*x for x in img.size)
img = img.resize(new_size, Image.ANTIALIAS)
print(pytesseract.image_to_string(img))
'''
