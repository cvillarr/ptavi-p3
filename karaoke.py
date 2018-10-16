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

try:
    fichsmil = sys.argv[1]
    fichjson = sys.argv[1].replace(".smil",".json")
    archivosmil = []

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open(fichsmil))
    listval = cHandler.get_tags()

    with open (fichjson, "w") as fichero_json:
    
        #creando archivo
        for linea in listval:
            listatotal = []
            listattr = []
            etiq = linea[0]
            atributos = linea[1]
            listattr.append(etiq)
            for attr in atributos:
                listattr.append(attr + "=" + '"' + atributos[attr] + '"')
            listattr = "\t".join(listattr)
            archivosmil.append(listattr + "\n")
        
        """#json
        fichero_json = json.dumps(archivosmil)"""

        for linea in listval:
            atributos = linea[1]
            for attr,valor in atributos.items():
                if attr == "src" and valor[:7] == "http://":
                    nombre = valor.split("/")[-1]
                    urlretrieve(valor, nombre)
                    print ("Descargando %s ..." % valor)
                    print (nombre)

except IndexError:
    sys.exit("Usage:python3 karaoke.py file.smil")












