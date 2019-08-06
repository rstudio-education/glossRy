#!/usr/bin/env python

import sys
import re


PAT_REFERENCED = re.compile(r'\[.+?\]\(#(.+?)\)', re.MULTILINE + re.DOTALL)
PAT_DEFINED = re.compile(r'^(.+?):\n:', re.MULTILINE)


def main(reader):
    data = reader.read()
    referenced = PAT_REFERENCED.findall(data)
    defined = [slugify(term) for term in PAT_DEFINED.findall(data)]
    missing = set(referenced) - set(defined)
    for m in sorted(missing):
        print(m)


def slugify(term):
    return term.lower().replace(' ', '-').replace('(', '').replace(')', '')
        

if __name__ == '__main__':
    if len(sys.argv) == 1:
        main(sys.stdin)
    elif len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as reader:
            main(reader)
    else:
        print('Usage: check.py [filename]', file=sys.stderr)
        sys.exit(1)
