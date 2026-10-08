import pytest

from network_toolkit.ports import get_port_information


def test_well_known_port():
    result = get_port_information(443)

    assert result["port"] == 443
    assert result["category"] == "well-known"


def test_registered_port():
    result = get_port_information(8080)

    assert result["port"] == 8080
    assert result["category"] == "registered"


def test_dynamic_port():
    result = get_port_information(50000)

    assert result["port"] == 50000
    assert result["category"] == "dynamic/private"


def test_port_zero():
    result = get_port_information(0)

    assert result["port"] == 0
    assert result["category"] == "well-known"


def test_maximum_port():
    result = get_port_information(65535)

    assert result["port"] == 65535
    assert result["category"] == "dynamic/private"


def test_negative_port():
    with pytest.raises(ValueError):
        get_port_information(-1)


def test_port_above_maximum():
    with pytest.raises(ValueError):
        get_port_information(65536)


def test_non_integer_port():
    with pytest.raises(TypeError):
        get_port_information("443")