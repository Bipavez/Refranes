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


'''
print(pytesseract.image_to_string(Image.open(f'refranes/refranes-002.png'), lang='spa'))
print('\n==============\n')
print(pytesseract.image_to_string(Image.open(f'img/pag2.png'), lang='spa'))
'''
for n in range(1,101):
    with open('raws/pag{:0>3d}.txt'.format(n), 'w') as pag:
        pag.write(pytesseract.image_to_string(Image.open('refranes/refranes-{:0>3d}.png'.format(n)), lang='spa'))


'''
Esto es una weaita que toy testeando xd


img = Image.open('testx.png')
print(pytesseract.image_to_string(img), '\n----\n')
new_size = tuple(2*x for x in img.size)
img = img.resize(new_size, Image.ANTIALIAS)
print(pytesseract.image_to_string(img))
'''
