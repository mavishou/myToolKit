#!/usr/bin/env python2.7
# -*- coding: utf-8 -*

'''
This script is used to get the entire gene annotation from trans.gtf
'''

import gtf_util as gtf
import sys
# import pdb

def summaryLast():
	global curGeneId
	global curCh
	global curSrc
	global curStrand
	global lCoords

	# pool all coordinates together, the min is the first, the max is the last
	# pdb.set_trace()
	lCoords = [int(c) for c in lCoords]
	firstCoord = min(lCoords)
	lastCoord = max(lCoords)

	lOut = [curCh, curSrc, 'gene', str(firstCoord), str(lastCoord), '.', curStrand, '.', 'gene_id "' + curGeneId + '";']
	print '\t'.join(lOut)


curGeneId = ''

# f = open('/lustre/user/houm/projects/AnnoLnc/test_trans.gtf')
# for line in f.readlines():
for line in sys.stdin.readlines():
	li = line.rstrip('\n').split('\t')
	# pdb.set_trace()
	dAnnos = gtf.processAnnotation(li[8])
	transId = dAnnos['transcript_id']
	geneId = dAnnos['gene_id']

	if geneId != curGeneId and curGeneId != '':
		summaryLast()

	if geneId != curGeneId:
		curGeneId = geneId
		curCh, curSrc = li[0:2]
		curStrand = li[6]
		lCoords = []

	lCoords += li[3:5]

summaryLast()



