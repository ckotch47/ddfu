from app import DnsBruteforceService, DnsResolverService
from print_color import print
import argparse
import pyfiglet

parser = argparse.ArgumentParser(description='Program for dns resolve')
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
    help='bruteforce subdomain'
)
parser.add_argument(
    '-p',
    type=str,
    default='worldlist/subdomains-100.txt',
    required=False,
    help='path for wordlist txt'
)
parser.add_argument(
    '-r',
    type=bool,
    default=False,
    required=False,
    action=argparse.BooleanOptionalAction,
    help='recursive depth for bruteforce subdomain'

)
m_arguments = parser.parse_args()


def main(arguments):
    dns_resolve = DnsResolverService()
    dns_bruteforce = DnsBruteforceService()
    dns_bruteforce.debug = False

    depth = 1 if arguments.r else 0

    if not arguments.host:
        return

    if not arguments.b:
        dns_resolve.resolve(arguments.host, show_failed=True)
    else:
        dns_bruteforce.bruteforce_domain(arguments.host, arguments.p, depth)
        dns_bruteforce.print_domains()


if __name__ == '__main__':
    print(
        pyfiglet.figlet_format("dns seen", font="slant"),
        color='c'
    )
    main(m_arguments)

