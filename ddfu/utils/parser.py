import argparse

epilog_text = '''
        python main.py --host google.com                                                : for find ip and dns recon
        python main.py --host google.com -b -p worldlist/subdomain.txt                  : for find ip and dns recon and bruteforce subdomain
        python main.py --host google.com -b -p worldlist/subdomain.txt -r               : for find ip and dns recon and bruteforce subdomain and find bigger subdomain
        python main.py --host http://localhost --port 8000 -ddos -t 10                  : for simple ddos server
        python main.py --host http://localhost -admin -p 'admin-page.txt' -timeout 0.3  : for simple adminfinder or swagger finder
        python main.py --ip 192.168.0.1                                                 : try find hosting server
        python main.py --host google.com -map                                           : for scan port on host
        python main.py --ip 192.168.0.1 -map                                            : for scan port on ip    
        python main.py -fuzz --url https://example/FUZZ --header '{"Authorization": ""}': for fuzz
        --method get --body '{"id":"FUZZUUID4", "docs": "fuzz"}' -p fuzz.txt
    
'''

parser = argparse.ArgumentParser(
    description='Program for dns resolve and ddos server by url',
    epilog=epilog_text,
    formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument(
    '--host',
    type=str,
    default=None,
    help='host for resolve'
)

parser.add_argument(
    '-b',
    type=bool,
    default=False,
    required=False,
    action=argparse.BooleanOptionalAction,
    help='bruteforce subdomain for resolve dns'
)
parser.add_argument(
    '-p',
    type=str,
    default='worldlist/subdomains-100.txt',
    required=False,
    help='path for wordlist subdomain txt for resolve dns'
)
parser.add_argument(
    '-r',
    type=bool,
    default=False,
    required=False,
    action=argparse.BooleanOptionalAction,
    help='recursive depth for bruteforce subdomain'
)

parser.add_argument(
    '--port',
    type=int,
    default=80,
    help='port for resolve in ddos'
)
parser.add_argument(
    '-ddos',
    type=bool,
    default=False,
    required=False,
    action=argparse.BooleanOptionalAction,
    help='active ddos atack'
)
parser.add_argument(
    '-t',
    type=int,
    default=10,
    help='user count for ddos'
)

parser.add_argument(
    '-admin',
    type=bool,
    default=False,
    required=False,
    action=argparse.BooleanOptionalAction,
    help='active adminfinder panel'
)
parser.add_argument(
    '-timeout',
    type=float,
    default=0.1,
    help='timeout for request adminfinder'
)
parser.add_argument(
    '--ip',
    type=str,
    default=None,
    help='ip for find host'
)
parser.add_argument(
    '-map',
    type=bool,
    default=False,
    required=False,
    action=argparse.BooleanOptionalAction,
    help='active port scan for --ip'
)

parser.add_argument(
    '-fuzz',
    type=bool,
    default=False,
    required=False,
    action=argparse.BooleanOptionalAction,
    help='active fuzzing attack'
)
parser.add_argument(
    '--url',
    type=str,
    default=None,
    help='url for fuzz'
)
parser.add_argument(
    '--method',
    type=str,
    default=None,
    help='method get for fuzz (get, post, put, patch, delete)'
)
parser.add_argument(
    '--header',
    type=str,
    default=None,
    help='add header params to fuzzing (json string)'
)
parser.add_argument(
    '--body',
    type=str,
    default=None,
    help='add body params to post method to fuzzing (json string)'
)
m_arguments = parser.parse_args()
