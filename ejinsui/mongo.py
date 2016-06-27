# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import pymongo

from config import MONGO_URI, MONGO_DB

mongo_client = pymongo.MongoClient(MONGO_URI)
mongo_db = mongo_client[MONGO_DB]


class CompanyDB(object):
    def __init__(self):
        pass

    @staticmethod
    def upsert_company(item):
        mongo_db['company_info'].update({
            'cname': item['cname']
        }, item, True, True)
