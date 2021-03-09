def validIPAddress(IP):
    if not IP: return "Neither"

    def is_ipv4(s):
        ip = IP.split('.')
        for s in ip:
            if len(s) == 0 or len(s) > 3:
                return 'Neither'
            if ((s[0] == '0' and len(s) != 1) or not s.isdigit() or int(s) > 255):
                return 'Neither'
        return 'IPv4'

    def is_ipv6(s):
        ip = IP.split(':')
        for s in ip:
            if len(s) == 0 or len(s) > 4:
                return "Neither"
            for c in s:
                if c not in '0123456789abcdefABCDEF':
                    return "Neither"
        return 'IPv6'

    if len(IP.split('.')) == 4:
        return is_ipv4(IP)
    if len(IP.split(':')) == 8:
        return is_ipv6(IP)
    else:
        return 'Neither'
