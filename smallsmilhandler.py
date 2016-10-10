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
        return self.atributos


if __name__ == "__main__":
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil.xml'))
    
    Dicc = cHandler.get_tags()
    print(Dicc)

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):
	
	def __init__(self):
		self.dicc = {}
		self.etiquetas = {"root-layout","region","img","audio","textstream"}

		self.atributos = {
			"root-layout": ["width", "height", "background-color"],
			"region": ["id", "top", "bottom", "left", "right"],
			"img": ["scr", "region", "begin", "dur"],
			"audio": ["scr", "begin", "dur"],
			"textstream": ["scr", "region"]
			}
	
	def startElement(self, name, attrs):
		if name in self.etiquetas:
			
			
			

if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil.xml'))


