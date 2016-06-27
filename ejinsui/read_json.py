# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import json


def read_file(filename):
    f = open(filename)
    all_text = f.readall()
    return all_text


def read_json(filename):
    all_text = read_file(filename)
    json_text =  all_text.rsplit("ws('list',", 2)[1].lsplit("PT.wid('list')", 2)[0]
    json_list = json.loads(json_text)
    return json_list