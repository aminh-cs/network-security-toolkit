import ipaddress


def get_ip_information(ip_address: str) -> dict:
    """Return basic information about an IP address."""

    ip = ipaddress.ip_address(ip_address)

    return {
        "address": str(ip),
        "version": ip.version,
        "is_private": ip.is_private,
        "is_global": ip.is_global,
        "is_loopback": ip.is_loopback,
        "is_multicast": ip.is_multicast,
    }