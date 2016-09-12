# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import pymongo

# MONGO
MONGO_URI = "localhost:27017"
MONGO_DB = "ejinsui"

mongo_client = pymongo.MongoClient(MONGO_URI)
mongo_db = mongo_client[MONGO_DB]


class CompanyDB(object):
    def __init__(self):
        pass

    @staticmethod
    def upsert_company(item):
        print '<MONGO> %s' % item
        mongo_db.company_info.update({'cname': item['cname']}, item, True, True)
