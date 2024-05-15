from ddfu.src import DnsBruteforceService, DnsResolverService, run_ddos_request, AdminFinder, dns_get_ptr, PortScan, Fuzzing
from print_color import print
import pyfiglet

from ddfu.utils.parser import m_arguments


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


def main():
    arguments = m_arguments
    print(
        pyfiglet.figlet_format("DDFu", font="larry3d"),
        color='c'
    )
    try:
        if arguments.ddos:
            run_ddos_request(arguments.host, arguments.port, arguments.t)
            return
        if arguments.admin:
            AdminFinder().admin_finder_request(arguments.host, arguments.timeout, arguments.p)
            return
        if arguments.ip and not arguments.map:
            dns_get_ptr.get(arguments.ip)
            dns_get_ptr.print()
            return
        if arguments.ip and arguments.map:
            PortScan().scan(arguments.ip)
            return
        if arguments.host and arguments.map:
            host_ip = DnsResolverService().resolve(arguments.host, show_failed=True)
            PortScan().scan(host_ip)
            return
        if arguments.fuzz:
            Fuzzing(arguments.url, arguments.method,  arguments.header, arguments.body, arguments.p, arguments.timeout).fuzz()
            return
        main_dns_resolve(arguments)
    except KeyboardInterrupt:
        print('exit by user', color='r')
        return
    except Exception as e:
        print(e)
        return

# poetry run ddfu -fuzz --url https://app.vtpad.ru/space/FUZZ --header "{Auth: admin}" --method get --body "{id:'1', docs: 'fuzz'}"

