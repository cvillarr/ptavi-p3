#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 11:02:00 2018

@author: cvillarr
"""
import sys

from xml.sax import make_parser
from smallsmilhandler import SmallSMILHandler


try:
    fichsmil = sys.argv[1]
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open(fichsmil))
    listval = cHandler.get_tags()

    for linea in listval:
        listatotal = []
        listattr = []
        etiq = linea[0]
        atributos = linea[1]
        listattr.append(etiq)
        for attr in atributos:
            listattr.append(attr + "=" + '"' + atributos[attr] + '"')
        listattr = "\\".join(listattr)

        print (listattr)


except IndexError:
    sys.exit("Usage:python3 karaoke.py file.smil")
    











