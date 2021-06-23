#!/usr/bin/env python3

import sys
import ldif
import hashlib
from collections import OrderedDict


def freeze(o):
    if isinstance(o, dict):
        return OrderedDict({k: freeze(v) for k, v in sorted(o.items())}.items())
    if isinstance(o, list):
        return sorted(o)
    return o


ldifparser = ldif.LDIFRecordList(sys.stdin)
ldifparser.parse()

data = {k: v for k, v in ldifparser.all_records}
f = freeze(data)

h = hashlib.sha256(str(f).encode('utf-8')).hexdigest()
print(h)
