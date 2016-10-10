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
            "img": ["src", "region", "begin", "dur"],
            "audio": ["src", "begin", "dur"],
            "textstream": ["src", "region"]
            }

    def startElement(self, name, attrs):
        if name in self.etiquetas:
            dicc = {}
            for etiqueta in self.etiquetas[name]:
                dicc[etiqueta] = attrs.get(etiqueta, "")
            self.atributos.append([name, dicc])

    def get_tags(self):
        return(self.atributos)


if __name__ == "__main__":
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil.xml'))

    print(cHandler.get_tags())
