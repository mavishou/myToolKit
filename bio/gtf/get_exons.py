#!/usr/bin/python
'''
Get exon lines of each gtf file and simplify the 9th col
'''

import sys
from gtf_util import processGTFAnno as processAnnotation

for line in sys.stdin.readlines():
	line = line.rstrip('\n')
	# exclude comment lines
	if not line.startswith('#'):
		line = line.split('\t')
		if line[2] == 'exon':
			dAnno = processAnnotation(line[8])
			line[8] = 'gene_id \"' + dAnno['gene_id'] + '\"; transcript_id \"' + dAnno['transcript_id'] + '\";'
			outLine = '\t'.join(line)
			print outLine
	dAnno = []
