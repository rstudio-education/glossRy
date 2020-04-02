#!/usr/bin/env python

import sys
import re
import yaml


USAGE = 'check.py [/path/to/glossary.yml]'
REQUIRED = ['slug', 'term']
LANGUAGES = {
    'en': 'English'
}
CROSSREF = re.compile(r'\[.+?\]\(#(.+?)\)')


def main(text):
    '''Check contents of glossary.'''

    content = yaml.load(text, Loader=yaml.Loader)
    known = set([entry['slug'] for entry in content])

    # All entries have required keys.
    for entry in content:
        for req in REQUIRED:
            check(req in entry,
                  f'Require {req} in entry {entry}')

    # Entries are alphabetical.
    actual = [entry['term'].lower() for entry in content]
    sorted = actual[:]
    sorted.sort()
    for [a, s] in zip(actual, sorted):
        check(a == s,
              f'Terms {a} and {s} are not in alphabetical order')

    # Cross-references.
    for entry in content:
        slug = entry['slug']

        # External cross-references resolve.
        if 'see' in entry:
            for key in entry['see']:
                check(key in known,
                      f'Bad cross-reference {key} in {slug}')

        # Internal cross-references resolve.
        for lang in LANGUAGES:
            if lang in entry:
                for crossref in CROSSREF.findall(entry[lang]):
                    check(crossref in known,
                          f'Bad cross-reference {crossref} in {LANGUAGES[lang]} body of {slug}')


def check(test, msg):
    '''Report violation of a single check.'''
    if not test:
        print(msg)


def fail(msg):
    '''Fail due to internal error.'''
    print(msg, file=sys.stderr)
    sys.exit(1)


# Main driver.
if __name__ == '__main__':
    if len(sys.argv) == 1:
        main(sys.stdin.read())
    elif len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as reader:
            main(reader.read())
    else:
        fail(USAGE)
