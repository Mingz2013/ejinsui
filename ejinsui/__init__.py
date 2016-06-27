# -*- coding:utf-8 -*-
__author__ = 'zhaojm'
import os

from mongo import CompanyDB
from read_json import read_json

def run(rootdir):
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            # print rootdir, filename
            try:
                json_list = read_json(rootdir + '/' + filename)
                for json_obj in json_list:
                    # CompanyDB.upsert_company(json_obj)
                    # print json_obj
                    pass
            except Exception, e:
                print e.message
