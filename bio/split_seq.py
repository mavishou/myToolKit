#!/usr/bin/python

import sys
import getopt
from Bio import SeqIO
import math

def usage():
	print 'Split a fasta file into several small files.'
	print
	print 'Usage:\t' + sys.argv[0] + ' -i input.fa [-n INT]'
	print
	print '\t-i\tThe file you want to split'
	print '\t-n\tThe number of files you want to split.\t[10]'

fastaFile = ''
num = 10
opts, args = getopt.getopt(sys.argv[1:], 'i:n:h:')
for op, value in opts:
	if op == '-i':
		fastaFile = value
	elif op == '-n':
		num = value
	elif op == '-h':
		usage()
		sys.exit()
	else:
		sys.stderr.write('Unknown arguments!\n')
		usage()
		sys.exit(1)

if fastaFile == '':
	sys.stderr.write('-i must be specified!\n')
	print
	usage()
	sys.exit(1)

try:
	num = int(num)
except Exception as e:
	sys.stderr.write('-n should be an integer.\n')
	print
	usage()
	sys.exit(1)

# get the count
fFasta = open(fastaFile)
count = 0
for record in SeqIO.parse(fFasta, 'fasta'):
	count += 1
fFasta.close()

# deal with file_name
lFileName = fastaFile.split('.')
if len(lFileName) > 1:
	baseName = '.'.join(lFileName[:-1])
	suffix = lFileName[-1]
else:
	baseName = lFileName
	suffix = ''

# get the seq num of each file
eachNum = int(math.ceil(float(count) / num))
iCount = 0
fileNum = 1
fFasta = open(fastaFile)
wSplit = open(baseName + '_' + str(fileNum) + '.' + suffix, 'w')
for record in SeqIO.parse(fFasta, 'fasta'):
	iCount += 1
	if iCount > eachNum:
		wSplit.close()
		fileNum += 1
		wSplit = open(baseName + '_' + str(fileNum) + '.' + suffix, 'w')
		iCount = 1
	wSplit.write('>' + record.id + '\n')
	wSplit.write(str(record.seq) + '\n')
fFasta.close()
wSplit.close()

