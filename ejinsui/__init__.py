# -*- coding:utf-8 -*-
__author__ = 'zhaojm'
import os

from mongo import CompanyDB
from read_json import read_json

def run(rootdir):
    i = 0
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            # print rootdir, filename
            try:
                json_list = read_json(rootdir + '/' + filename)
                # print json_list
                for json_obj in json_list:
                    d_o = dict(json_obj)
                    d_o.update({'insert_20160912': 1})
                    CompanyDB.upsert_company(d_o)
                    i += 1
                    print i
                    pass
            except Exception, e:
                print e.message
