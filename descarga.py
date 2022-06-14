import requests
from os import remove
mylist = [["es.xml", 'https://i.mjh.nz/PlutoTV/es.xml', 'es'],
          ["mx.xml", 'https://i.mjh.nz/PlutoTV/mx.xml', 'mx'],
          ["sam.xml", 'https://i.mjh.nz/SamsungTVPlus/es.xml', '']]
i = 1
primera = ""
otras = ""

def insertar_texto(cadena, texto):
    posicion = cadena.find('<programme channel="')
    if posicion <= len(cadena):
        izquierda = cadena[:posicion]
        derecha = cadena[posicion:]

        return '{} {} {}'.format(izquierda, texto, derecha)
    else:
        raise ValueError(
            'La posición donde se quiere insertar el texto no existe.')

def ejecuta_descarga():
    i = 1

    for x in mylist:
        url = x[1]
        myfile = requests.get(url)
        open(x[0], 'wb').write(myfile.content)
        f = open(x[0], 'r', encoding="utf8")

        if i == 1:
            primera = f.read()
            f.close()
            primera = primera.replace('<channel id="', '<channel id="' +
                                    x[2]).replace('<programme channel="', '<programme channel="'+x[2]).replace("</display-name>", "_"+x[2]+"</display-name>")
        else:
            otras = f.read()
            f.close()
            otras = otras[otras.find('<channel id="'):]
            otras = otras.replace('<channel id="', '<channel id="' +
                                x[2]).replace('<programme channel="', '<programme channel="'+x[2]).replace("</display-name>", "_"+x[2]+"</display-name>")
            otras = otras.replace("</tv>", "")
            primera = insertar_texto(primera, otras)
        
        i = i+1
    primera = insertar_texto(primera, otras)

    f = open('todo.xml', 'w', encoding="utf8")
    f.write(primera.replace('></desc>', '>nn</desc>'))
    f.close()


ejecuta_descarga()

