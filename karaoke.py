#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 11:02:00 2018

@author: cvillarr
"""
import sys
import json


from xml.sax import make_parser
from smallsmilhandler import SmallSMILHandler
from urllib.request import urlretrieve


class KaraokeLocal():

    def __init__(self, fich):
        parser = make_parser()
        cHandler = SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(fichsmil))
        self.listval = cHandler.get_tags()

    def __str__(self):
        archivosmil = []
        for linea in self.listval:
            listattr = []
            etiq = linea[0]
            atributos = linea[1]
            listattr.append(etiq)
            for attr in atributos:
                listattr.append(attr + "=" + '"' + atributos[attr] + '"')
            listattr = "\t".join(listattr)
            archivosmil.append(listattr + "\n")
        print(archivosmil)

    def to_json(self, fichjson):
        with open(fichjson, "w"):
            json.dumps(self.listval)

    def do_local(self):
        for linea in self.listval:
            atributos = linea[1]
            for attr, valor in atributos.items():
                if attr == "src" and valor[:7] == "http://":
                    nombre = valor.split("/")[-1]
                    urlretrieve(valor, nombre)
                    print("Descargando %s ..." % valor)


if __name__ == "__main__":
    try:
        fichsmil = sys.argv[1]
        fichjson = sys.argv[1].replace(".smil", ".json")
        fichkaraokeloc = KaraokeLocal(fichsmil)
        fichkaraokeloc.__str__()
        fichkaraokeloc.to_json(fichjson)
        fichkaraokeloc.do_local()
        fichkaraokeloc.to_json('local.json')
        fichkaraokeloc.__str__()

    except IndexError:
        sys.exit("Usage:python3 karaoke.py file.smil")
