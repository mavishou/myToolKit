#!/usr/bin/python
'''
extract locations of transcripts from a gtf file
'''

import sys
from gtf_util import processAnnotation
import numpy as np

# flncrnaGTF = open('annolnc_lncRNA_v1_exon.gtf')
# wlncRNALoc = open('annolnc_lncrna_location_v1.txt', 'w')

flncrnaGTF = open(sys.argv[1])
wlncRNALoc = open(sys.argv[2], 'w')

def sortExons(llExons):
	npExons = np.array(llExons)
	idx = np.lexsort((npExons[:,1],npExons[:,0]))
	llsortedExons = npExons[idx].tolist()
	return llsortedExons

def getLoc():
	global curTrans, gene, chr, strand, llExons, lCoords
	lCoords.sort()
	llsortedExons = sortExons(llExons)
	lExons = []
	for i in range(len(llsortedExons)):
		lExons.append(str(llsortedExons[i][0]) + '-' + str(llsortedExons[i][1]))
	coords = ','.join(lExons)
	lLoc = [chr, strand, coords]
	loc = ';'.join(lLoc)
	lOut = [curTrans, gene, str(lCoords[0]), str(lCoords[-1]), loc]
	wlncRNALoc.write('\t'.join(lOut) + '\n')

dLncrna = {}
curTrans = ''

for row in flncrnaGTF.readlines():
	cols = row.rstrip('\n').split('\t')
	dAnno = processAnnotation(cols[8])
	trans = dAnno['transcript_id']

	if trans != curTrans:
		if curTrans != '':
			getLoc()

		curTrans = trans
		gene = dAnno['gene_id']
		chr = cols[0]
		strand = cols[6]
		llExons = []
		lCoords = []
	left = int(cols[3])
	right = int(cols[4])
	llExons.append([left, right])
	lCoords.extend([left, right])

getLoc()
