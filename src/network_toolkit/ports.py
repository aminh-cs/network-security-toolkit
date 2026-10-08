def get_port_information(port: int) -> dict:
    """Return basic information about a network port."""

    if not isinstance(port, int):
        raise TypeError("port must be an integer")

    if not 0 <= port <= 65535:
        raise ValueError("port must be between 0 and 65535")

    if port <= 1023:
        category = "well-known"
    elif port <= 49151:
        category = "registered"
    else:
        category = "dynamic/private"

    return {
        "port": port,
        "category": category,
    }