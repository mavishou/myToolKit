#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Created by Hou Mei on 2016/12/15

from myToolKit.general_helper import *


def main():
    total_len = 0
    for line in sys.stdin:
        l_line = line_to_list(line)
        start = int(l_line[3])
        end = int(l_line[4])
        total_len += (end - start + 1)
    print total_len

if __name__ == '__main__':
    main()
