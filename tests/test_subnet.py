from network_toolkit.subnet import get_subnet_information


def test_ipv4_subnet():
    result = get_subnet_information("192.168.1.0/24")

    assert result["network"] == "192.168.1.0"
    assert result["broadcast"] == "192.168.1.255"
    assert result["netmask"] == "255.255.255.0"
    assert result["prefix_length"] == 24
    assert result["num_addresses"] == 256
    assert result["version"] == 4
def test_ipv4_small_subnet():
    result = get_subnet_information("10.0.0.0/30")

    assert result["network"] == "10.0.0.0"
    assert result["broadcast"] == "10.0.0.3"
    assert result["netmask"] == "255.255.255.252"
    assert result["prefix_length"] == 30
    assert result["num_addresses"] == 4
    assert result["version"] == 4
def test_ipv6_subnet():
    result = get_subnet_information("2001:db8::/64")

    assert result["network"] == "2001:db8::"
    assert result["prefix_length"] == 64
    assert result["version"] == 6