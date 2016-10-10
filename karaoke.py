#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler

import sys

def Lectura_Karaoke(lista):
    dicc = ""
    for element in lista:
        dicc =  dicc + element[0]
        elemento = element[1]
        for name in elemento:
            dicc = dicc + '\t' + name + '=' + '"' + elemento.get(name) + '"'
        dicc = dicc + '\n'

    print(dicc)


if __name__ == "__main__":

    archivo = sys.argv[1]

    try:
        arch = open(archivo, 'r')
    except:
        sys.exit("Usage: python3 karaoke.py file.smil.")

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open(archivo))
    
    lista = cHandler.get_tags()
    Lectura_Karaoke(lista)
