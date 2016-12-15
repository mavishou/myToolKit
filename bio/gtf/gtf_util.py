#!/usr/bin/env python2.7
# -*- coding: utf-8 -*
'''
Author: Mei Hou
This script contains some useful functions
'''
import sys


def processGTFAnno(anno):
    dAnnos = {}
    annos = anno.split(';')
    annos = [a.strip() for a in annos if a != '' and a != ' ']
    for a in annos:
        lA = a.split(' ')
        if len(lA) > 2:
            print 'The annotation is not in the right format: %s' % anno
            print lA
            sys.exit(1)
        dAnnos[lA[0]] = lA[1].strip('"')
    return (dAnnos)

