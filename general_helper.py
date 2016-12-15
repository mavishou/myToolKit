import os
import sys
import json
import logging
import subprocess
from collections import OrderedDict
from copy import copy


def line_to_list(line):
    return line.rstrip('\n').split('\t')


def remove_first_line(reader):
    reader.readline()
    return reader


def get_output_line(l_line):
    return '\t'.join(l_line) + '\n'


def file_to_list(f):
    out_list = []
    with open(f) as reader:
        for line in reader:
            out_list.append(line.rstrip('\n'))
    return out_list


def list_to_file(li, output_file):
    with open(output_file, 'w') as writer:
        for l in li:
            writer.write(l + '\n')


def prepare_dir(d):
    if not os.path.exists(d):
        os.makedirs(d)


def exit_with_run_info(error_reason='', exit_code=1):
    output_log = {'exit_code': exit_code,
                  'error_reason': error_reason}
    if exit_code == 2:
        output_log['error_msg'] = 'System error.'
    else:
        output_log['error_msg'] = error_reason
    print json.dumps(output_log)
    sys.exit(exit_code)


def split_line():
    logging.info('------------------------------------------------')


def run_cmd(simple_cmd, task_name, run_dir=None):
    logging.info('Running %s...' % task_name)
    # cmd = '(time %s) >%s 2>&1' % (simple_cmd, log_file)
    cmd = simple_cmd
    logging.info(cmd)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=run_dir)
    exit_code = p.wait()
    logging.info(p.stdout.read())

    if exit_code != 0:
        error_msg = 'Run %s fails.' % task_name
        exit_with_run_info(error_msg, 2)
    else:
        logging.info('%s done!' % task_name)


def initialize_ordered_dict_table(row_list, colunm_list, value=0):
    od_table = OrderedDict()
    for row_name in row_list:
        od_row = OrderedDict()
        for col_name in colunm_list:
            od_row[col_name] = value
        od_table[row_name] = od_row
    return od_table


def initialize_ordered_dict_list(li, value=0):
    od_list = OrderedDict()
    for l in li:
        od_list[l] = copy(value)
    return od_list


def output_str_list_as_one_line(s, l, writer):
    l_out = [s]
    l_out.extend(l)
    writer.write(get_output_line(l_out))


def str_list(l):
    return [str(e) for e in l]
