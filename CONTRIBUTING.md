# Contributing

Our goal is to make this glossary available
both as a web page
and as a package in R and Python
so that the following will work:

```
# In R
> library(glossry)
> define('fully qualified name')

An unambiguous name of the form `package::thing`.
```

```
# In Python
>>> from glossary import define
>>> define('singleton')

A set with only one element, or a class with only one instance.
```

By submitting material, you are agreeing to abide by our [Code of Conduct](CONDUCT.md)
and to make your contribution available under the terms of our [license](LICENSE.md).
All contributors will be acknowledged by name unless they request otherwise.

## Structure

Terms are defined in `_data/glossary.yml` in order to be compatible with [GitHub Pages][ghp].
The format of this YAML file is explained below.
To add, extend, amend, or correct a definition, please:

1.  [File an issue][issues] with the term as the title and the suggested change as the issue body,
    or

2.  [Create a pull request][pr] with the term as the title and the suggested change as a modification to `_data/glossary.yml`.

3.  Please tag all issues and PRs:
    -   `enhancement` for new material.
    -   `alteration` for changes to existing material.
    -   `requested` for a definition you would like but don't feel able to write.
    -   `question` and `help wanted` for questions and matters requiring assistance respectively.

4.  Please put `FIXME` in the text where work is needed.
    (We are particularly grateful for contributions that fill in existing `FIXME` markers.)

## YAML Format

Each term is currently defined by a block of YAML formatted as follows:

```
- term: some word or phrase (REQUIRED)
  slug: unique-hyphenated-lowercase-id (REQUIRED)
  en: >
    A paragraph of English, usually indented below the 'en' key to allow line
    wrapping. (Notice the '>' after the 'en' key, which tells YAML to expect a
    paragraph.) This text should use Markdown formatting, and [word](#some-slug)
    for embedded cross-references.
  es: >
    Spanish definition.  Use 'de', 'fr', 'jp', etc. for other languages.
  acronym: XYZ (OPTIONAL)
  see: (OPTIONAL)
    - some-other-slug
    - and-yet-another-slug
  links: (OPTIONAL)
  - title: Your First Reference (REQUIRED)
    link: http://some/thing (REQUIRED)
```

This format will evolve as we discover new requirements.

1.  Please add new terms in alphabetical order.

2.  Please put special strings like "null" in quotation marks
    (because [Norway][norway]).

## Checking

Use `bin/check.py _data/glossary.yml` to check the format and consistency of the glossary.
Enhancements to this script are greatly appreciated.

[ghp]: https://pages.github.com
[issues]: https://github.com/rstudio-education/glossRy/issues
[norway]: https://third-bit.com/2015/06/11/why-we-cant-have-nice-things.html
[pr]: https://github.com/rstudio-education/glossRy/pulls
