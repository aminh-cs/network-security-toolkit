import pytest
from network_toolkit.ip_utils import get_ip_information


def test_private_ipv4_address():
    result = get_ip_information("192.168.1.10")

    assert result["address"] == "192.168.1.10"
    assert result["version"] == 4
    assert result["is_private"] is True
    assert result["is_loopback"] is False
    assert result["is_multicast"] is False
def test_public_ipv4_address():
    result = get_ip_information("8.8.8.8")

    assert result["address"] == "8.8.8.8"
    assert result["version"] == 4
    assert result["is_private"] is False
    assert result["is_global"] is True


def test_loopback_address():
    result = get_ip_information("127.0.0.1")

    assert result["address"] == "127.0.0.1"
    assert result["version"] == 4
    assert result["is_loopback"] is True


def test_ipv6_address():
    result = get_ip_information("2001:4860:4860::8888")

    assert result["address"] == "2001:4860:4860::8888"
    assert result["version"] == 6
    assert result["is_global"] is True


def test_multicast_address():
    result = get_ip_information("224.0.0.1")

    assert result["address"] == "224.0.0.1"
    assert result["version"] == 4
    assert result["is_multicast"] is True
import pytest
def test_invalid_ip_address():
    with pytest.raises(ValueError):
        get_ip_information("not-an-ip-address")