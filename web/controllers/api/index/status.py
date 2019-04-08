import requests
from tornado import gen
from tornado.web import RequestHandler

VJ_URL = {
    'HDU': 'http://acm.hdu.edu.cn',
    'POJ': 'http://poj.org/',
    'SDUT': 'http://acm.sdut.edu.cn/'
}


class Handler(RequestHandler):
    """
    检查vj状态
    """

    @gen.coroutine
    def get(self, vj):
        ret = 'False'
        try:
            r = requests.get(VJ_URL[vj], timeout=3)
            if r.status_code == 200:
                ret = 'True'
        except Exception:
            pass
        self.write(ret)
