import argparse

from .ip_utils import get_ip_information
from .ports import get_port_information
from .subnet import get_subnet_information
from .connectivity import check_tcp_connectivity


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Network Security Toolkit"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    ip_parser = subparsers.add_parser(
        "ip",
        help="Analyze an IP address",
    )
    ip_parser.add_argument(
        "address",
        help="IPv4 or IPv6 address",
    )

    subnet_parser = subparsers.add_parser(
        "subnet",
        help="Analyze a network subnet",
    )
    subnet_parser.add_argument(
        "network",
        help="IPv4 or IPv6 network in CIDR notation",
    )

    port_parser = subparsers.add_parser(
        "port",
        help="Analyze a network port",
    )
    port_parser.add_argument(
        "port",
        type=int,
        help="Port number from 0 to 65535",
    )

    check_parser = subparsers.add_parser(
        "check",
        help="Check TCP connectivity to a host and port",
    )
    check_parser.add_argument(
        "host",
        help="Hostname or IP address",
    )
    check_parser.add_argument(
        "port",
        type=int,
        help="TCP port number",
    )
    check_parser.add_argument(
        "--timeout",
        type=float,
        default=3.0,
        help="Connection timeout in seconds (default: 3)",
    )

    args = parser.parse_args()

    try:
        if args.command == "ip":
            result = get_ip_information(args.address)
        elif args.command == "subnet":
            result = get_subnet_information(args.network)
        elif args.command == "port":
            result = get_port_information(args.port)
        else:
            result = check_tcp_connectivity(
                args.host,
                args.port,
                timeout=args.timeout,
            )

    except (TypeError, ValueError) as error:
        parser.error(str(error))
    for key, value in result.items():
        print(f"{key}: {value}")