import pytest

from network_toolkit.cli import main


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