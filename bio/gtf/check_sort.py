#!/usr/bin/env python2.7
# -*- coding: utf-8 -*
'''Check whether a GTF file is well sorted by gene_id and transcript_id'''

import sys
import gtf_util as gtf
from collections import defaultdict

ddGene = defaultdict(int)
ddTrans = defaultdict(int)
curTransId = ''
curGeneId = ''
okTrans = 1
okGene = 1

for line in sys.stdin.readlines():
	li = line.rstrip('\n').split('\t')
	dAnnos = gtf.processGTFAnno(li[8])
	lineTransId = dAnnos['transcript_id']
	lineGeneId = dAnnos['gene_id']
	
	if lineTransId != curTransId:
		curTransId = lineTransId
		ddTrans[curTransId] += 1
	
	if lineGeneId != curGeneId:
		curGeneId = lineGeneId
		ddGene[curGeneId] += 1

for k, v in ddGene.items():
	if v > 1:
		sys.stderr.write(k + ' is not well sorted!\n')
		okGene = 0
if okGene == 1:
	print 'The file is well sorted by genes!'

for k, v in ddTrans.items():
	if v > 1:
		sys.stderr.write(k + ' is repeated!\n')
		okTrans = 0

if okTrans == 1:
	print 'The file is well sorted by transcripts!'
