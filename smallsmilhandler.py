#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__(self):

        self.atributos = []
        self.etiquetas = {
            "root-layout": ["width", "height", "background-color"],
            "region": ["id", "top", "bottom", "left", "right"],
            "img": ["scr", "region", "begin", "dur"],
            "audio": ["scr", "begin", "dur"],
            "textstream": ["scr", "region"]
            }

    def startElement(self, name, attrs):
        if name in self.etiquetas:
            dicc = {}
            for etiqueta in self.etiquetas[name]:
                dicc[etiqueta] = attrs.get(etiqueta, "")
            self.atributos.append([name, dicc])

    def get_tags(self):
        print(self.atributos)


if __name__ == "__main__":
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil.xml'))

    cHandler.get_tags()

