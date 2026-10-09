# Network Security Toolkit

[![Tests](https://github.com/aminh-cs/network-security-toolkit/actions/workflows/tests.yml/badge.svg)](https://github.com/aminh-cs/network-security-toolkit/actions/workflows/tests.yml)

A Python command-line toolkit for IP address analysis, subnet calculations, port classification, and TCP connectivity testing.

Built as a practical project to strengthen my understanding of computer networking, Python, and network security fundamentals.

## Features

- **IP analysis:** Identify IP version, private/global status, loopback status, and multicast status.
- **Subnet analysis:** Calculate network address, broadcast address, netmask, prefix length, and address count.
- **Port classification:** Classify port numbers into well-known, registered, and dynamic/private ranges.
- **TCP connectivity checks:** Attempt a TCP connection to a specified host and port, with configurable timeout handling.
- **Input validation:** Handle invalid addresses, subnet definitions, port numbers, and timeouts.
- **Automated tests:** Unit and CLI tests using `pytest`, including mocked socket connections.

## Requirements

- Python 3.11 or newer
- Git
- `pytest` for running tests

## Installation

Clone the repository and enter the project directory:

```bash
git clone https://github.com/aminh-cs/network-security-toolkit.git
cd network-security-toolkit
```

Create and activate a virtual environment.

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the project in editable mode:

```powershell
python -m pip install -e . --no-build-isolation
```

If you plan to run the tests, install the test dependency:

```powershell
python -m pip install pytest
```

## Usage

Run commands from the project directory with the virtual environment activated.

### Analyze an IP address

```powershell
python -m network_toolkit ip 192.168.1.10
```

Example output:

```text
address: 192.168.1.10
version: 4
is_private: True
is_global: False
is_loopback: False
is_multicast: False
```

### Analyze a subnet

```powershell
python -m network_toolkit subnet 192.168.1.0/24
```

Example output:

```text
network: 192.168.1.0
broadcast: 192.168.1.255
netmask: 255.255.255.0
prefix_length: 24
num_addresses: 256
version: 4
```

### Classify a port

```powershell
python -m network_toolkit port 443
```

Example output:

```text
port: 443
category: well-known
```

Port categories follow these numeric ranges:

| Range | Category |
|---|---|
| 0–1023 | Well-known |
| 1024–49151 | Registered |
| 49152–65535 | Dynamic/private |

### Check TCP connectivity

```powershell
python -m network_toolkit check 127.0.0.1 443 --timeout 3
```

The command reports the host, port, whether a TCP connection was established, and the result status.

A timeout means a connection was not established within the configured time. It does not, by itself, prove that a port is closed.

## Run the tests

```powershell
python -m pytest -v
```

The current test suite contains 31 tests covering IP analysis, subnet calculations, port classification, TCP connectivity behavior, input validation, and CLI commands.

## Project structure

```text
network-security-toolkit/
├── src/
│   └── network_toolkit/
│       ├── __init__.py
│       ├── __main__.py
│       ├── cli.py
│       ├── connectivity.py
│       ├── ip_utils.py
│       ├── ports.py
│       └── subnet.py
├── tests/
│   ├── test_cli.py
│   ├── test_connectivity.py
│   ├── test_ip_utils.py
│   ├── test_ports.py
│   └── test_subnet.py
├── .gitignore
├── pyproject.toml
├── README.md
└── requirements.txt
```

## Limitations

- TCP connectivity results depend on network conditions, firewalls, routing, and the target service.
- A successful connection does not establish that a service is secure.
- Port classification is based on numeric ranges, not on whether a particular service is actually running.
- Automated connectivity tests use mocked sockets; they do not constitute an end-to-end network test.

## Future improvements

- Add structured logging and more detailed error reporting.
- Add JSON output for integration with other tools.
- Expand network monitoring and traffic-analysis capabilities.
- Add further tests for edge cases and command-line behavior.

## Author

**Amin Heidari Pourafshar**

Computer Science graduate interested in cybersecurity, network security, and secure infrastructure.

GitHub: [aminh-cs](https://github.com/aminh-cs)
