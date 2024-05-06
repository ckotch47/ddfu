import asyncio

from app import DnsBruteforceService, DnsResolverService, run_ddos_request
from print_color import print
import pyfiglet

from utils.parser import m_arguments


def main_dns_resolve(arguments):
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
    return


async def main(arguments):
    if arguments.ddos:
        run_ddos_request(arguments.host, arguments.port, arguments.t)
        return
    main_dns_resolve(arguments)


if __name__ == '__main__':
    print(
        pyfiglet.figlet_format("dsd", font="slant"),
        color='c'
    )
    asyncio.run(main(m_arguments))
