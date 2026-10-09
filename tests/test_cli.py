import pytest

from network_toolkit.cli import main
from unittest.mock import patch


def test_ip_command(capsys, monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        ["network-toolkit", "ip", "192.168.1.10"],
    )

    main()

    captured = capsys.readouterr()

    assert "address: 192.168.1.10" in captured.out
    assert "version: 4" in captured.out
    assert "is_private: True" in captured.out


def test_subnet_command(capsys, monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        ["network-toolkit", "subnet", "192.168.1.0/24"],
    )

    main()

    captured = capsys.readouterr()

    assert "network: 192.168.1.0" in captured.out
    assert "broadcast: 192.168.1.255" in captured.out
    assert "prefix_length: 24" in captured.out
    assert "num_addresses: 256" in captured.out


def test_invalid_ip_command(capsys, monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        ["network-toolkit", "ip", "999.999.999.999"],
    )

    with pytest.raises(SystemExit):
        main()

    captured = capsys.readouterr()

    assert "does not appear to be an IPv4 or IPv6 address" in captured.err


def test_port_command(capsys, monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        ["network-toolkit", "port", "443"],
    )

    main()

    captured = capsys.readouterr()

    assert "port: 443" in captured.out
    assert "category: well-known" in captured.out


def test_port_out_of_range(capsys, monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        ["network-toolkit", "port", "65536"],
    )

    with pytest.raises(SystemExit):
        main()

    captured = capsys.readouterr()

    assert "port must be between 0 and 65535" in captured.err
def test_check_command(capsys, monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        ["network-toolkit", "check", "127.0.0.1", "443"],
    )

    with patch(
        "network_toolkit.connectivity.socket.create_connection"
    ) as mock_connect:
        mock_connect.return_value.__enter__.return_value = None
        main()

    captured = capsys.readouterr()

    assert "host: 127.0.0.1" in captured.out
    assert "port: 443" in captured.out
    assert "reachable: True" in captured.out
    assert "status: connected" in captured.out


def test_check_invalid_port(capsys, monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        ["network-toolkit", "check", "127.0.0.1", "65536"],
    )

    with pytest.raises(SystemExit):
        main()

    captured = capsys.readouterr()

    assert "port must be between 1 and 65535" in captured.err