import re
import os


def pasapalabra(pag):
    #uhm, a esta función pasemosle el texto q sale de pytesseract
    pattern = "(?<=(\n){2}|.\n|^..)([a-zA-Z,\. \-:áéíóúÁÉÍÓÚñÑ\(\)]*)(\n)?(?=\n([a-zA-Z 0-9áéíóúÁÉÍÓÚñÑ]){0,5}((?i)([a-z]){3}(\.|,)( )?(?i)([a-z])(\.|,)( )?(?i)([a-z])(\.|,)|(?i)([a-z]){3}(\.|,)( )?([0-9]){3}|([a-zA-Z]){2}\.:))"
    prelista = (item[1].rstrip("\n") for item in re.findall(pattern, pag))
    resultado = filter(lambda x: x, prelista)
    return resultado
if __name__ == '__main__':
    # with open("full.txt", "w", encoding = "utf8") as file:
    #     for i in range(1, 101):
    #         with open("raws_bw/pag{:0>3d}.txt".format(i), "r", encoding = "utf8") as page:
    #             file.write(page.read()+"\n")
    #
    # with open("jiji.txt", "w", encoding="utf8") as file:
    #     for i in range(1, 101):
    #         with open("raws_bw/pag{:0>3d}.txt".format(i), "r", encoding="utf8") as page:
    #             file.write("\n".join([*pasapalabra(page.read())])+"\n")
    with open("jiji.txt", "r", encoding="utf8") as file:
        obj =  file.read().split("\n")
    n = sum(map(lambda x: len(x), obj))/len(obj)
    print("Promedio de refranes es %f" %n)
    
