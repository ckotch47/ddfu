import time

import requests
from src.common import header_service
from print_color import print


class AdminFinder:
    def __init__(self, filename):
        self.wordlist = self.open(filename)
        self.index = 0
        self.max = len(self.wordlist)

    def open(self, filename):
        try:
            with open(filename) as filehandle:
                return [line.strip('\n') for line in filehandle.readlines()]
        except Exception as e:
            print(e, color='red')
            exit(1)

    def __iter__(self):
        self.index = 0
        return self
    def __len__(self):
        return self.max

    def __next__(self):
        if self.index >= self.max:
            raise StopIteration
        else:
            word = self.wordlist[self.index]
            self.index += 1
            return word


def _request(url, host):
    return requests.get(
        url=f'{url}'
    )


def admin_finder_request(url: str, timeout: int = 0, filename: str = 'worldlist/admin-page.txt'):
    adminFinder = AdminFinder(filename)
    for i in range(adminFinder.max):
        i = adminFinder.__next__()
        if not i:
            break
        res = _request(f"{url}/{i}", url)
        if res.status_code == 200:
            print(f"{url}/{i}", tag_color='g', tag=f'{res.status_code}')
        else:
            print(f"{url}/{i}", tag_color='r', tag=f'{res.status_code}')
        time.sleep(timeout)
