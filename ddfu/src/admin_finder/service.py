import time

import requests
from print_color import print
from ddfu.src.common.file_base import FileBase


# class AdminFinder:
#     def __init__(self, filename):
#         self.wordlist = self.open(filename)
#         self.index = 0
#         self.max = len(self.wordlist)
#
#     def open(self, filename):
#         try:
#             with open(filename) as filehandle:
#                 return [line.strip('\n') for line in filehandle.readlines()]
#         except Exception as e:
#             print(e, color='red')
#             exit(1)
#
#     def __iter__(self):
#         self.index = 0
#         return self
#
#     def __len__(self):
#         return self.max
#
#     def __next__(self):
#         if self.index >= self.max:
#             raise StopIteration
#         else:
#             word = self.wordlist[self.index]
#             self.index += 1
#             return word

class AdminFinder:

    def _request(self, url, host):
        return requests.get(
            url=f'{url}'
        )

    def admin_finder_request(self, url: str, timeout: int = 0, filename: str = 'worldlist/admin-page.txt'):
        file_base = FileBase(filename)
        for i in file_base.__iter__():
            if not i:
                break
            res = self._request(f"{url}/{i}", url)
            if res.status_code == 200:
                print(f"{url}/{i}", color='c', tag_color='g', tag=f'{res.status_code}')
            else:
                print(f"{url}/{i}", color='c', tag_color='r', tag=f'{res.status_code}')
            time.sleep(timeout)
