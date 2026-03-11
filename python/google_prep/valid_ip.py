'''
Validate IP Address
Validate an IP address (IPv4). An address is valid if and only if it is in the form "X.X.X.X", where each X is a number from 0 to 255.

For example, "12.34.5.6", "0.23.25.0", and "255.255.255.255" are valid IP addresses, while "12.34.56.oops", "1.2.3.4.5", and "123.235.153.425" are invalid IP addresses.

Examples:

ip = '192.168.0.1'
output: true

ip = '0.0.0.0'
output: true

ip = '123.24.59.99'
output: true

ip = '192.168.123.456'
output: false

'''


def validateIP(ip: str) -> bool:
    parts = ip.split('.')
    if len(parts) != 4:
        return False

    for p in parts:
        if p == "":
            return False

        if not p.isdigit():
            return False
        if len(p) > 1 and p[0] == 0:
            return False
        val = int(p)
        if val < 0 and val > 255:
            return False
    return True
	
# debug your code below
print(validateIP('192.168.0.1'))