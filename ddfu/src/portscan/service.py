import socket
from print_color import print
from ddfu.src.common.progress_bar_base import ProgressBarBase
from ddfu.src.common.file_base import FileBase

class PortScan:
    def __init__(self):
        self.bar = None
        socket.setdefaulttimeout(0.05)
        self.udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.data = b'h'
        self.port_file = FileBase('worldlist/topports.txt')
        self.res_tcp = []
        self.res_udp = []

    def scan(self, host):
        self.bar = ProgressBarBase(self.port_file.__len__(), 'Scan port')
        for port in self.port_file.__iter__():
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if not tcp.connect_ex((host, int(port))):
                self.res_tcp.append(port)
                tcp.close()
            try:
                self.udp.sendto(self.data, (host, int(port)))
                self.udp.settimeout(0)
                if self.udp.recvfrom(1024):
                    self.res_udp.append(port)
            except:
                pass
            self.bar.__next__()
        self.bar.__del__()
        self.print_port()
        return

    def print_port(self):
        for i in self.res_tcp:
            print(i, color='c', tag_color='g', tag=f"tcp")
        for i in self.res_udp:
            print(i, color='c', tag_color='y', tag=f"udp")