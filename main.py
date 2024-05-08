from src import DnsBruteforceService, DnsResolverService, run_ddos_request, admin_finder_request, dns_get_ptr
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


def main(arguments):
    print(
        pyfiglet.figlet_format("DDFu", font="larry3d"),
        color='c'
    )
    if arguments.ddos:
        run_ddos_request(arguments.host, arguments.port, arguments.t)
        return
    if arguments.admin:
        admin_finder_request(arguments.host, arguments.timeout, arguments.p)
        return
    if arguments.ip:
        dns_get_ptr.get(arguments.ip)
        dns_get_ptr.print()
        return
    main_dns_resolve(arguments)


main(m_arguments)
