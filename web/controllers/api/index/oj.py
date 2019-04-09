import json
import threading

import requests
from tornado import gen
from tornado.web import RequestHandler
import pymongo
import config

class Handler(RequestHandler):
    """
    获得oj list
    """

    @gen.coroutine
    def get(self):
        oj_list = yield self._find_OJ()
        ret = []
        for oj in oj_list:
            oj = {
                'name': oj.get('soj'),
                'url': oj.get('url'),
                'status': oj.get('status')
            }
            ret.append(oj)
        self.write(json.dumps(ret))
        for oj in oj_list:
            threading.Thread(target=upate_status, args=(oj,)).start()

    @gen.coroutine
    def _find_OJ(self):
        cnt = yield self.settings["database"]["OJ"].count()
        return (yield self.settings["database"]["OJ"].find().to_list(cnt))


def upate_status(oj):
    status = check_status(oj)
    db = pymongo.MongoClient(config.dbhost)[config.dbname]
    db["OJ"].update({
        '_id': oj.get('_id')
    }, {
        '$set': {'status': str(status)}
    })


def check_status(oj):
    status = 'Remote OJ Error'
    try:
        r = requests.get(oj.get('url'), timeout=3)
        if r.status_code == 200:
            status = 'Working'
    except Exception:
        pass
    return status
