# glossRy

A small glossary of terms used in R and data science, designed for novices who
are still orienting themselves.  Contributions are very welcome: please see [the
contribution guidelines](CONTRIBUTING.md) if you would like to lend and hand,
and please note that all contributors must abide by our [Code of
Conduct](CONDUCT.md).

## Definitions

**absolute path**: A path that points to the same location in the filesystem
  regardless of where it's evaluated. An absolute path is the equivalent of
  latitude and longitude in geography. See also *relative path*.

**aggregation function**: A function that combines many values into one, such as
  `sum` or `max`.

**base R**: FIXME

**Cascading Style Sheets**: A way to describe how HTML should be rendered.

**character encoding**: A specification of how characters are stored as
  bytes. The most commonly-used encoding today is *UTF-8*.

**closure**: A set of variables defined in the same *scope* whose existence has
  been preserved after that scope has ended. Closures are one of the trickiest
  ideas in programming.

**Comma-Separated Values**: A text format for tabular data in which each record
  is one row and fields are separated by commas. There are many minor
  variations, particularly around quoting of strings.

**data frame**: FIXME

**escape sequence**: A sequence of characters used to represent some other
  character that would otherwise have a special meaning. For example, the escape
  sequence `\"` is used to represent a double-quote character inside a
  double-quoted string.

**exception**: An object that stores information about an error or other unusual
  event in a program. One part of a program will create and *throw* an exception
  to signal that something unexpected has happened; another part will *catch*
  it.

**falsy**: A horrible neologism meaning "equivalent to false". See also the
  equally horrible *truthy*.

**functional programming**: A style of programming in which data is transformed
  through successive application of functions, rather than by using control
  structures such as loops. Functional programming in R relies heavily on
  *higher-order functions*.

**global installation**: Installing a package in a location where it can be
  accessed by all users and projects. See also *local installation*.

**global variable**: A variable defined outside any particular function, which
  is therefore visible to all functions. See also *local variable*.

**GNU Public License**: A license that allows people to re-use software as long
  as they distribute the source of their changes.

**header row**: If present, the first of a *CSV* file that defines column names
  (but tragically, not their data types or units).

**heterogeneous**: Having mixed type. For example, an *array* is said to be
  heterogeneous if it contains a mix of numbers, character strings, and values
  of other types. See also *homogeneous*.

**higher-order function**: A function that operates on other functions. For
  example, the higher-order function `map` executes a given function once on
  each value in an *list*. Higher-order functions are heavily used in
  *functional programming*.

**homogeneous**: Having a single type. For example, an *array* is said to be
  homogeneous if it contains only numbers or only character strings, but not a
  mix of the two.

**Integrated Development Environment (IDE)**: FIXME

**JSON**: A way to represent data by combining basic values like numbers and
  character strings in *arrays* and name/value structures. The acronym stands
  for "JavaScript Object Notation"; unlike better-defined standards like *XML*,
  it is unencumbered by a syntax for comments or ways to define *schemas*.

**lazy evaluation**: see *non-standard evaluation*.

**list**: FIXME.

**local installation**: Placing a package inside a particular project so that it
  is only accessible within that project. See also *global installation*.

**local variable**: A variable defined inside a function which is only visible
  within that function. See also *global variable* and *closure*.

**MIT License**: A license that allows people to re-use software with no
**restrictions.  mutation**: Changing data in place, such as modifying an
**element of an array or adding a record to a database.

**name collision**: The ambiguity that arises when two or more things in a
  program that have the same name are active at the same time. The *call stack*
  was invented in part to address this problem.

**non-standard evaluation**: FIXME.

**NoSQL database**: Any database that doesn't use the *relational* model.  The
  awkward name comes from the fact that such databases don't use *SQL* as a
  query language.

**package**: FIXME

**package manager**: A program that does its best to keep track of the bits and
  bobs of software installed on a computer.

**parameter**: A variable whose value is passed into a function when the
  function is called. Some writers distinguish parameters (the variables) from
  *arguments* (the values passed in), but others use the terms in the opposite
  sense. It's all very confusing.

**parse**: To translate the text of a program or web page into a data structure
  in memory that the program can then manipulate.

**production code**: Software that is delivered to an end user. The term is used
  to distinguish such code from test code, deployment infrastructure, and
  everything else that programmers write along the way.

**pseudo-random number**: A value generated in a repeatable way that has the
  properties of being truly random.

**pseudo-random number generator**: A function that can generate a series of
  *pseudo-random numbers* after being initialized with a *seed*.

**R Markdown**: FIXME

**raise**: To signal that something unexpected or unusual has happened in a
  program by creating an *exception* and handing it to the error-handling
  system, which then tries to find a point in the program that will *catch* it.

**read-evaluate-print loop**: An interactive program that reads a command typed
  in by a user, executes it, prints the result, and then waits patiently for the
  next command. REPLs are often used to explore new ideas or for debugging.

**regular expression**: A pattern for matching text, written as text
  itself. Regular expressions are sometimes called "regexp", "regex", or "RE",
  and are as powerful as they are cryptic.  See [this
  documentation][regular-expression-doc] for more details.

**relational database**: A database that organizes information into *tables*,
  each of which has a fixed set of named *fields* (shown as columns) and a
  variable number of *records* (shown as rows). See also *SQL*.

**relative path**: A path whose destination is interpreted relative to some
  other location, such as the current directory. A relative path is the
  equivalent of giving directions using terms like "straight" and "left". See
  also *absolute path*.

**root directory**: The directory that contains everything else, directly or
  indirectly. The root directory is written `/` (a bare forward slash).

**scalar**: FIXME

**scope**: The portion of a program within which a definition can be seen and
  used. See *global-variable*, *local-variable*, and *closure*.

**script**: FIXME

**seed**: A value used to initialize a *pseudo-random number generator*.

**SQL**: The language used for writing queries for *relational databases*. The
  term was originally an acronym for Structured Query Language.

**string**: A block of text in a program. The term is short for "character
  string".

**string interpolation**: The process of inserting text corresponding to
  specified values into a string, usually to make output human-readable.

**table**: A set of uniformly-formatted *records* in a *relational database*.
  Tables are usually drawn with rows (each of which represents one record) and
  columns (each of which represents a *field*).

**tibble**: FIXME

**tidy data**: FIXME

**tidyverse**: FIXME

**truthy**: A truly Orwellian neologism meaning "not equivalent to false". See
  also *falsy*, but only if you are able to set aside your respect for the
  English language.

**Unicode**: A standard that defines numeric codes for many thousands of
  characters and symbols. Unicode does not define how those numbers are stored;
  that is done by standards like *UTF-8*.

**unit test**: A test that exercises one property or expected behavior of a
  system.

**UTF-8**: A way to store the numeric codes representing Unicode characters in
  memory that is *backward-compatible* with the older *ASCII* standard.

**variable**: A name in a program that has some data associated with it. A
  variable's value can be changed after definition. See also *constant*.

**vector**: FIXME

**whitespace**: The space, newline, carriage return, and horizontal and vertical
  tab characters that take up space but don't create a visible mark.  The name
  comes from their appearance on a printed page in the era of typewriters.

## Contributors

-   [Greg Wilson](http://third-bit.com)

[regular-expression-doc]: https://stringr.tidyverse.org/articles/regular-expressions.html
