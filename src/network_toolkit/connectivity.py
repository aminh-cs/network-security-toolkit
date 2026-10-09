import socket


def check_tcp_connectivity(
    host: str,
    port: int,
    timeout: float = 3.0,
) -> dict:
    """Check whether a TCP connection can be established."""

    if not isinstance(host, str) or not host.strip():
        raise ValueError("host must be a non-empty string")

    if not isinstance(port, int) or isinstance(port, bool):
        raise TypeError("port must be an integer")

    if not 1 <= port <= 65535:
        raise ValueError("port must be between 1 and 65535")

    if timeout <= 0:
        raise ValueError("timeout must be greater than 0")

    try:
        with socket.create_connection((host, port), timeout=timeout):
            return {
                "host": host,
                "port": port,
                "reachable": True,
                "status": "connected",
            }
    except socket.timeout:
        status = "timeout"
    except ConnectionRefusedError:
        status = "connection refused"
    except OSError as error:
        status = f"connection failed: {error}"

    return {
        "host": host,
        "port": port,
        "reachable": False,
        "status": status,
    }