def ip_to_int32(ip):
    return sum(int(x) << (8 * (3 - i)) for i, x in enumerate(ip.split('.')))