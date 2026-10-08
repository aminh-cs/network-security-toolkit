import ipaddress


def get_subnet_information(network: str) -> dict:
    """Return basic information about an IPv4 or IPv6 network."""

    subnet = ipaddress.ip_network(network, strict=False)

    return {
        "network": str(subnet.network_address),
        "broadcast": str(subnet.broadcast_address),
        "netmask": str(subnet.netmask),
        "prefix_length": subnet.prefixlen,
        "num_addresses": subnet.num_addresses,
        "version": subnet.version,
    }