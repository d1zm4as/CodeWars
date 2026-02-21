import re
def size_to_number(s):
    if s == 'm': return 38
    if re.match('^x*s$',s): return 38 - 2 * len(s)
    if re.match('^x*l$',s): return 38 + 2 * len(s)