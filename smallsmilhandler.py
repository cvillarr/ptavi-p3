#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):

        self.rootlayout = {'width': '', 'height': '', 'background-color': ''}
        self.region = {'id': '', 'top': '', 'bottom': '', 'left': '',
                       'right': ''}
        self.img = {'src': '', 'region': '', 'begin': '', 'dur': ''}
        self.audio = {'src': '', 'begin': '', 'dur': ''}
        self.textstream = {'src': '', 'region': ''}
        self.listaetiq = ['root-layout', 'region', 'img', 'audio',
                          'textstream']
        self.listafinal = []

    def startElement(self, name, attrs):
        if name == 'root-layout':
            dicc_aux = {}
            for attr in self.rootlayout:
                dicc_aux[attr] = attrs.get(attr, '')
            self.listafinal.append([name, dicc_aux])
        elif name == 'region':
            dicc_aux = {}
            for attr in self.region:
                dicc_aux[attr] = attrs.get(attr, '')
            self.listafinal.append([name, dicc_aux])
        elif name == 'img':
            dicc_aux = {}
            for attr in self.img:
                dicc_aux[attr] = attrs.get(attr, '')
            self.listafinal.append([name, dicc_aux])
        elif name == 'audio':
            dicc_aux = {}
            for attr in self.audio:
                dicc_aux[attr] = attrs.get(attr, '')
            self.listafinal.append([name, dicc_aux])
        elif name == 'textstream':
            dicc_aux = {}
            for attr in self.textstream:
                dicc_aux[attr] = attrs.get(attr, '')
            self.listafinal.append([name, dicc_aux])

    def get_tags(self):
        return self.listafinal


if __name__ == "__main__":
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    print(cHandler.get_tags())
