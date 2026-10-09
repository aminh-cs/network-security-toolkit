import socket
from unittest.mock import patch

import pytest

from network_toolkit.connectivity import check_tcp_connectivity


def test_successful_connection():
    with patch("network_toolkit.connectivity.socket.create_connection") as mock_connect:
        mock_connect.return_value.__enter__.return_value = None

        result = check_tcp_connectivity("127.0.0.1", 443)

    assert result["host"] == "127.0.0.1"
    assert result["port"] == 443
    assert result["reachable"] is True
    assert result["status"] == "connected"


def test_connection_refused():
    with patch(
        "network_toolkit.connectivity.socket.create_connection",
        side_effect=ConnectionRefusedError,
    ):
        result = check_tcp_connectivity("127.0.0.1", 443)

    assert result["reachable"] is False
    assert result["status"] == "connection refused"


def test_connection_timeout():
    with patch(
        "network_toolkit.connectivity.socket.create_connection",
        side_effect=socket.timeout,
    ):
        result = check_tcp_connectivity("127.0.0.1", 443)

    assert result["reachable"] is False
    assert result["status"] == "timeout"


def test_invalid_port():
    with pytest.raises(ValueError):
        check_tcp_connectivity("127.0.0.1", 65536)


def test_port_must_be_integer():
    with pytest.raises(TypeError):
        check_tcp_connectivity("127.0.0.1", "443")


def test_empty_host():
    with pytest.raises(ValueError):
        check_tcp_connectivity("", 443)


def test_invalid_timeout():
    with pytest.raises(ValueError):
        check_tcp_connectivity("127.0.0.1", 443, timeout=0)