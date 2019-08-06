#!/usr/bin/env python

import sys
import re


PAT_ALL = re.compile(r'\*\*(.+?)\*\*', re.MULTILINE + re.DOTALL)
PAT_DEFINED = re.compile(r'^\*\*(.+?)\*\*', re.MULTILINE + re.DOTALL)
PAT_SPACE = re.compile(r'\s+', re.MULTILINE)


def main(reader):
    data = reader.read()
    all_terms = get(data, PAT_ALL)
    defined_terms = get(data, PAT_DEFINED)
    missing = set(all_terms) - set(defined_terms)
    for m in sorted(missing):
        print(m)


def get(text, pattern):
    return [PAT_SPACE.sub(' ', t.lower()) for t in pattern.findall(text)]


if __name__ == '__main__':
    if len(sys.argv) == 1:
        main(sys.stdin)
    elif len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as reader:
            main(reader)
    else:
        print('Usage: check.py [filename]', file=sys.stderr)
        sys.exit(1)
