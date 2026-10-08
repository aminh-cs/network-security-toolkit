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