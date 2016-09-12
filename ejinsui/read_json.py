# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import json
import codecs


def read_file(filename):
    # f = open(filename, 'r')
    f = codecs.open(filename, 'r', 'utf-8')
    all_text = f.read()
    return all_text


def read_json(filename):
    all_text = read_file(filename)
    # print all_text
    if all_text.find(u"ws('list',") > -1:
        # print 'found', filename
        json_text = all_text.split(u"ws('list',")[1].split(u"); PT.wid('list')")[0]
        # print json_text
        json_list = json.loads(json_text)
        # print json_list
        return json_list
        # return json.loads('[]')
    else:
        # print 'not found', filename
        return json.loads('[]')
