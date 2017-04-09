#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Created by Hou Mei on 2016/12/18

import argparse
from myToolKit.general_helper import *
from myToolKit.bio.gtf.gtf_util import processGTFAnno
from collections import defaultdict


def main(input_gtf, output_file):
    d_gene_to_trans = defaultdict(set)
    d_gene_names = defaultdict(lambda: '-')
    d_trans_names = defaultdict(lambda: '-')

    with open(input_gtf) as reader:
        for line in reader:
            cols = line_to_list(line)
            d_annos = processGTFAnno(cols[8])
            gene_id = d_annos['gene_id']

            if 'gene_name' in d_annos:
                gene_name = d_annos['gene_name']
                d_gene_names[gene_id] = gene_name

            if 'transcript_id' in d_annos:
                trans_id = d_annos['transcript_id']
                d_gene_to_trans[gene_id].add(trans_id)
                if 'transcript_name' in d_annos:
                    trans_name = d_annos['transcript_name']
                    d_trans_names[trans_id] = trans_name

    with open(output_file, 'w') as writer:
        writer.write(get_output_line(['gene_id', 'gene_name', 'trans_id', 'trans_name']))
        for gene_id, transcripts in d_gene_to_trans.items():
            gene_name = d_gene_names[gene_id]
            for trans_id in transcripts:
                trans_name = d_trans_names[trans_id]
                out_line = [gene_id, gene_name, trans_id, trans_name]
                writer.write(get_output_line(out_line))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_gtf')
    parser.add_argument('output_file')
    args = parser.parse_args()

    main(args.input_gtf, args.output_file)
