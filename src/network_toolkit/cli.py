import argparse

from .ip_utils import get_ip_information
from .subnet import get_subnet_information


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

    args = parser.parse_args()

    try:
        if args.command == "ip":
            result = get_ip_information(args.address)
        else:
            result = get_subnet_information(args.network)

    except ValueError as error:
        parser.error(str(error))

    for key, value in result.items():
        print(f"{key}: {value}")