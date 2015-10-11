#!/usr/bin/env python2.7
# -*- coding: utf-8 -*
'''simplify a gtf file, only leave gene id and transcript id'''

import sys
from gtf_util import *

for line in sys.stdin.readlines():
	cols = line.rstrip('\n').split('\t')
	annos = processGTFAnno(cols[8])
	cols[8] = 'gene_id "%s"; transcript_id "%s"; ' % (annos['gene_id'], annos['transcript_id'])
	out = '\t'.join(cols)
	print out