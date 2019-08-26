---
layout: "default"
permalink: "/"
---

# glossRy

<h2 id="A">A</h2>

{:auto_ids}
Absolute path:
:   A path that points to the same location in the filesystem regardless of where
    it's evaluated. An absolute path is the equivalent of latitude and longitude
    in geography. See also [relative path](#relative-path).

Absolute row number:
:   The sequential index of a row in a table, regardless of what sections of the
    table is being displayed.

Aggregation:
:   To combine many values into one, e.g., by summing a set of numbers or
    concatenating a set of strings.

Aggregation function:
:   A function that combines many values into one, such as `sum` or `max`.

Aliasing:
:   To have two or more references to the same thing, such as a data structure
    in memory or a file on disk.

Anonymous function:
:   A function that has not been assigned a name.  Anonymous functions are usually
    quite short, and are usually defined where they are used, e.g., as
    callbacks.

Argument:
:   A value passed into a function. Some authors use the term as a synonym for
    [parameter](#parameter) and some do not; it's all very confusing.

ASCII:
:   A standard way to represent the characters commonly used in the Western
    European languages as 7- or 8-bit integers, now superceded by [Unicode](#unicode).

Attribute:
:   A name-value pair associated with an object, used to store metadata about the
    object such as an array's dimensions.

<h2 id="B">B</h2>

{:auto_ids}
Backward-compatible:
:   Software which is able to use earlier versions of itself (legacy) without problems.

Base R:
:   The basic functions making up the R language. See also [tidyverse](#tidyverse).

Binary:
:   FIXME

Binding:
:   FIXME

Branch:
:   A snapshot of a version of a Git repository. Multiple branches can capture
    multiple versions of the same repository. See also [feature branch](#feature-branch),
    [fork](#fork), [master branch](#master-branch).

<h2 id="C">C</h2>

{:auto_ids}
Call stack:
:   A data structure that stores information about the active subroutines
    executed. `cst()` is a useful function provided in the `lobstr` package to
    visualize a call stack.

Cascading Style Sheets (CSS):
:   A way to control the appearance of HTML.  CSS is typically used to specify
    fonts, colors, and layout.

Catch (exception):
:   To accept responsibility for handling an error or other unexpected event.  R
    prefers "handling a condition" to "catching an exception".  See also
    [condition](#condition), [handle](#handle-condition).

Character encoding:
:   A specification of how characters are stored as bytes. The most commonly-used
    encoding today is [UTF-8](#utf-8).

Class:
:   FIXME

Closure:
:   A set of variables defined in the same [scope](#scope) whose existence has been
    preserved after that scope has ended. Closures are one of the trickiest
    ideas in programming.

Coercion:
:   see [type coercion](#type-coercion).

Comma-Separated Values:
:   A text format for tabular data in which each record is one row and fields are
    separated by commas. There are many minor variations, particularly around
    quoting of strings.

Condition:
:   An error or other unexpected event that disrupts the normal flow of control.
    See also [handle](#handle-condition).

Constant:
:   FIXME

Constructor
:   of a class): A function that creates an object of a particular class.  In the
    [S3](#s3) object system, constructors are a convention rather than a
    requirement.

Copy-on-modify:
:   The practice of creating a new copy of aliased data whenever there is an
    attempt to modify it so that each reference will believe theirs is the only
    one.  See [aliasing](#aliasing).

CRAN:
:   The comprehensive R archive network (CRAN). Hosts R packages. See [base R](#base-R) [tidyverse](#tidyverse).

<h2 id="D">D</h2>

{:auto_ids}
Data frame:
:   A two-dimensional data structure for storing tabular data in memory.
    Rows represent [records](#record-database) and columns represent [variables](variable-data).
    See [tidy data](#tidy-data).

Double square brackets:
:   An index enclosed in `[[...]]`, used to return a single value of the
    underlying type.  See also [single square brackets](#single-square-brackets).

Data frame:
:   A class of objects that represents data and are typically used in fitting
    models.

Docker:
:   FIXME. See [backwards compatible](backwards-compatible) [version control system](version-control-system).

Double:
:   Short for "double-precision floating-point number", meaning a 64-bit numeric
    value with a fractional part and an exponent.

Dynamic scoping:
:   FIXME.  See [lexical scoping](#lexical-scoping).

<h2 id="E">E</h2>

{:auto_ids}
Eager evaluation:
:   FIXME.  See also [lazy evaluation](#lazy-evaluation).

Empty vector:
:   A vector that contains no elements.  Empty vectors have a type such as logical
    or character, and are *not* the same as [null](#null).

Environment:
:   A structure that stores a set of variable names and the values they refer to.

Escape sequence:
:   A sequence of characters used to represent some other character that would
    otherwise have a special meaning. For example, the escape sequence `\"` is
    used to represent a double-quote character inside a double-quoted string.

Evaluation:
:   The process of taking an expression such as `1+2*3/4` and turning it
    into a single irreducible value.

Exception:
:   An object that stores information about an error or other unusual event in a
    program. One part of a program will create and [raise](#raise) an exception to
    signal that something unexpected has happened; another part will [catch](#catch-exception)
    it.

<h2 id="F">F</h2>

{:auto_ids}
Falsy:
:   A horrible neologism meaning "equivalent to false". See also the equally
    horrible [truthy](#truthy).

Feature branch:
:   A branch within a Git repository containing commits dedicated to a specific feature, e.g. a bug fix or a new function. This branch can be merged into another branch. See [master branch](#master-branch).

Field (database):
:   FIXME

Fork:
:   A copy of one person's Git repository that lives in another person's GitHub
    account. Changes to the content of a fork can be submitted to the [upstream
    repository](#upstream-repository) via a [pull request](#pull-request). See
    also [branch](#branch).

Filter:
:   To choose a set of [records](#record-database) (i.e., rows of a table) based
    on the values they contain.

Fully-qualified name:
:   An unambiguous name of the form `package::thing`.

Functional programming:
:   A style of programming in which data is transformed through successive
    application of functions, rather than by using control structures such as
    loops.  See also [higher-order function](#higher-order-function)[object-oriented programming](#object-oriented-programming).

<h2 id="G">G</h2>

{:auto_ids}
Generic function:
:   A collection of functions with similar purpose, each operating on a different
    class of data.

Global environment:
:   The [environment](#environment) that holds top-level definitions in R, e.g., those written
    directly in the interpreter.

Global installation:
:   Installing a package in a location where it can be

Git:
:   a version control tool to record and manage changes to a project.

GitHub:
:   A cloud-based platform built around [Git](#git) that allows you to save versions
    of your project online and collaborate with other Git users.

Global installation:
:   Installing a package in a location where it can be accessed by all users and
    projects. See also [local installation](#local-installation).

Global variable:
:   A variable defined outside any particular function, which is therefore visible
    to all functions. See also [local variable](#local-variable).

Group:
:   To divide data into subsets according to some criteria while leaving records
    in a single structure.

GNU Public License:
:   A license that allows people to re-use software as long as they distribute the
    source of their changes.

<h2 id="H">H</h2>

{:auto_ids}
Handle (condition):
:   To accept responsibility for handling an error or other
    unexpected event.  R prefers "handling a condition" to "catching an
    exception".  See also [condition](#condition), [exception](#exception).

Header row:
:   If present, the first row of a CSV file that defines column names (but
    tragically, not their data types or units).  See also [comma-separated
    values](#comma-separated-values).

Heterogeneous:
:   Having mixed type. For example, an list can contain a mix of numbers,
    character strings, and values of other types. See also [homogeneous](#homogeneous).

Higher-order function:
:   A function that operates on other functions. For example, the higher-order
    function `map` executes a given function once on each value in an
    [list](#list). Higher-order functions are heavily used in [functional
    programming](#functional-programming).

Homogeneous:
:   Having a single type. For example, a [vector](#vector) must be homogeneous: its
    values must all be numeric, logical, etc.

Hubris:
:   Excessive pride or self-confidence.  See also [unit test](#unit-test) (lack of).

<h2 id="I">I</h2>

{:auto_ids}
Instance:
:   FIXME

Integrated Development Environment (IDE):
:   An application that helps programmers develop software.
    IDEs typically have a built-in editor, a console to execute code immediately,
    and browsers for exploring data structures in memory and files on disk.
    See also [Read-eval-print loop](#read-eval-print-loop-repl).

<h2 id="J">J</h2>

{:auto_ids}
JSON:
:   A way to represent data by combining basic values like numbers and character
    strings in lists and name/value structures. The acronym stands for
    "JavaScript Object Notation"; unlike better-defined standards like [XML](#xml),
    it is unencumbered by a syntax for comments or ways to define a [schema](#schema).

<h2 id="K">K</h2>

{:auto_ids}
knitr:
:   FIXME. See also [R markdown](#R-markdown).

<h2 id="L">L</h2>

{:auto_ids}
Lazy evaluation:
:   Delaying evaluation of an expression until the value is actually needed (or at
    least until after the point where it is first encountered).

Lexical scoping:
:   FIXME.  See [dynamic scoping](#dynamic-scoping).

Library:
:   See [package](#package).

List:
:   A [vector](#vector) that can contain values of many different types.

Literate programming:
:   A programming paradigm that mixes prose and code.  See also [R Markdown](#r-markdown).

Local installation:
:   Placing a package inside a particular project so that it is only accessible
    within that project. See also [global installation](#global-installation).

Local variable:
:   A variable defined inside a function which is only visible within that
    function. See also [closure](#closure), [global variable](#global-variable).

Logical indexing:
:   To index a vector or other structure with a vector of Booleans, keeping only
    the values that correspond to true values.  Also referred to as [masking](#masking).

<h2 id="M">M</h2>

{:auto_ids}
Markdown:
:   A markup language with a simple syntax created in 2004 supporting text-to-HTML. The language is readible as-is. It is often used for README files. See [R markdown](R-markdown)

Masking:
:   See [logical indexing](#logical-indexing).

Master branch:
:   A dedicated, permanent, central branch which should contain a "ready product". As a new feature is developed on a separate branch, to avoid breaking the main code, it can be merged into the master branch. See [feature-branch](feature-branch).

Merge (data):
:   FIXME

Merge (Git):
:   Merging branches in Git incorporates development histories of two branches in one. If changes are made to similar parts of the branches on both branches a commit will occur and this must be resolved before the merge will be completed.

Method:
:   An implementation of a [generic function](#generic-function) that handles objects of a specific class.

MIT License:
:   A license that allows people to re-use software with no restrictions.

Module:
:   See [package](#package).

Mutation:
:   Changing data in place, such as modifying an element of an array or adding a
    record to a database.

<h2 id="N">N</h2>

{:auto_ids}
NA:
:   A special value used to represent data that is not available.  See also [null](#null).

name collision:
:   The ambiguity that arises when two or more things in a program that have the
    same name are active at the same time. See also [call stack](#call-stack),
    [fully-qualified name](#fully-qualified-name).

Negative selection:
:   To specify the elements of a vector or other data structure that aren't
    desired by negating their indices.

Non-standard evaluation:
:   See [lazy evaluation](#lazy-evaluation).

NoSQL database:
:   Any database that doesn't use the relational model.  The awkward name comes
    from the fact that such databases don't use [SQL](#sql) as a query language.
    See also [relational database](#relational-database).

Null:
:   A special value used to represent a missing object.  `NULL` is not the same as
    `NA`, and neither is the same as an [empty vector](#empty-vector).

<h2 id="O">O</h2>

{:auto_ids}
Object-oriented programming:
:   FIXME

Observation:
:   FIXME

<h2 id="P">P</h2>

{:auto_ids}
Package:
:   A collection of code, data, and documentation that can be distributed and
    re-used.  Also referred to in some languages as a [library](#library) or
    [module](#module).

Package manager:
:   A program that does its best to keep track of the bits and bobs of software
    installed on a computer and their dependencies on one another.

Parameter:
:   A variable whose value is passed into a function when the function is
    called. Some writers distinguish parameters (the variables) from
    [arguments](#argument) (the values passed in), but others use the terms in the
    opposite sense. It's all very confusing.

Parse:
:   To translate the text of a program or web page into a data structure in memory
    that the program can then manipulate.

Peanuts:
:   An American comic strip by Charles M. Schulz which has inspired the names of R versions. 

Pipe operator:
:   The `%>%` used to make the output of one function the input of the next.

Prefix operator:
:   FIXME

Production code:
:   Software that is delivered to an end user. The term is used to distinguish
    such code from test code, deployment infrastructure, and everything else
    that programmers write along the way.

Pseudo-random numbers:
:   Value generated in a repeatable way that resemble the true randomness of the
    universe well enough to fool merely mortal observers.

Pseudo-random number generator:
:   A function that can generate [pseudo-random numbers](#pseudo-random-numbers).
    See also [seed](#seed).
    
Pull request:
:   The request to merge a new feature or correction created on a user's fork of a
    [Git](#git) repository into the [upstream repository](#upstream-repository). The
    developer will be notified of the change, review it, make or suggest
    changes, and potentially merge it. See also [fork](#fork).

Pull indexing:
:   Vectorized indexing in which the value at location `i` in the index vector
    specifies which element of the source vector is being pulled into that
    location in the result vector, i.e., `result[i] = source[index[i]]`.  See
    also [push indexing](#push-indexing).

Push indexing:
:   Vectorized indexing in which the value at location `i` in the index vector
    specifies an element of the result vector that gets the corresponding
    element of the source vector, i.e., `result[index[i]] = source[i]`.  Push
    indexing can easily produce gaps and collisions.  See also [pull
    indexing](#pull-indexing).

<h2 id="Q">Q</h2>

{:auto_ids}
Quosure:
:   A data structure containing an unevaluated expression and its environment.

Quoting function:
:   A function that is passed expressions rather than the values of those
    expressions.

<h2 id="R">R</h2>

{:auto_ids}
R Consortium:
:   FIXME

R Foundation:
:   Non-profit founded by the R development core team providing support for R. Is a member of the [R Consortium](#R-consortium).

R hub:
:   A free platform available to check a `R` package on several different
    platforms in preparation for the CRAN submission process.

R Markdown:
:   A dialect of [Markdown](#markdown) that allows authors to mix prose
    and code (usually written in R) in a single document.  See also
    [literate programming](#literate-programming).

Raise:
:   To signal that something unexpected or unusual has happened in a program by
    creating an [exception](#exception) and handing it to the error-handling system, which
    then tries to find a point in the program that will [catch](#catch-exception) it.

Reactive programming:
:   A style of programming in which actions are triggered by external events.

Reactive variable:
:   A variable whose value is automatically updated when some other value or
    values change.  Reactive variables are used extensively in [Shiny](#shiny).

Read-eval-print loop (REPL):
:   An interactive program that reads a command typed in by a user,
    executes it, prints the result, and then waits patiently for the next
    command. REPLs are often used to explore new ideas or for debugging.
    See also [Integrated Development Environment](#integrated-development-environment-ide).

Rebase:
:   FIXME

Record (database):
:   FIXME

Recycle:
:   To re-use values from a shorter vector in order to generate a sequence of the
    same length as a longer one.

Refactor (code):
:   FIXME

Refactor (R function):
:   FIXME

Regular expression:
:   A pattern for matching text, written as text itself. Regular expressions are
    sometimes called "regexp", "regex", or "RE", and are as powerful as they are
    cryptic.  See [this documentation][re-doc] for more details.

Relational database:
:   A database that organizes information into tables, each of which has a fixed
    set of named fields (shown as columns) and a variable number of records
    (shown as rows). See also [SQL](#sql), [table](#table).

Relative path:
:   A path whose destination is interpreted relative to some other location, such
    as the current directory. A relative path is the equivalent of giving
    directions using terms like "straight" and "left". See also [absolute
    path](#absolute-path).
    
Reprex:
:   A reproducible example. When asking questions about coding problems online or
    filing issues on GitHub, you should always include a reprex so others
    can reproduce your problem and help. The [reprex][reprex] package can help!

Relative row number:
:   The index of a row in a displayed portion of a table, which may or may not be
    the same as the [absolute row number](#absolute-row-number) within the table.

Repository:
:   A place where a [version control system](#version-control-system) stores
    the files that make up a project and the metadata that describes their history.
    See also [Git](#git), [GitHub](#github).

Root directory:
:   The directory that contains everything else, directly or indirectly. The root
    directory is written `/` (a bare forward slash).

<h2 id="S">S</h2>

{:auto_ids}
S:
:   A language originally developed in Bell Labs for data analysis, statistical
    modeling, and graphics. R is a dialect of S.

S3:
:   A framework for object-oriented programming in R.

S4:
:   A framework for object-oriented programming in R.

Scalar:
:   A single value of a particular type, such as 1 or "a".  Scalars don't really
    exist in R; values that appear to be scalars are actually vectors of unit
    length.

Scalar:
:   FIXME

Schema:
:   A specification of the format of a dataset, including the name, format, and
    content of each [table](#table).

Scope:
:   The portion of a program within which a definition can be seen and used. See
    [closure](#closure), [global variable](#global-variable), and [local variable](#local-variable).

Script:
:   Originally, a program written in a language too usable for "real" programmers
    to take seriously; the term is now synonymous with program.

Seed:
:   A value used to initialize a [pseudo-random number generator](#pseudo-random-number-generator).

Select:
:   To choose entire columns from a table by name or location.

Shiny:
:   FIXME

Signal
:   a condition): A way of indicating that something has gone wrong in a program,
    or that some other unexpected event has occurred.  R prefers "signalling a
    condition" to "raising an exception".

Single square brackets:
:   An index enclosed in `[...]`, used to select a structure from another
    structure.  See also [double square brackets](#double-square-brackets).

Singleton:
:   A set with only one element, or a [class](#class) with only one [instance](#instance).

SQL:
:   The language used for writing queries for a [relational database](#relational-database). The term
    was originally an acronym for Structured Query Language.

Squash
:   in Git): FIXME

Stack frame:
:   FIXME

String:
:   A block of text in a program. The term is short for "character string".

String interpolation:
:   The process of inserting text corresponding to specified values into a string,
    usually to make output human-readable.

<h2 id="T">T</h2>

{:auto_ids}
Table:
:   A set of records in a [relational database](#relational-database) or
    observations in a [data frame](#data-frame).  Tables are usually displayed
    as rows (each of which represents one [record](#record-database) or
    [observation](#observation)) and columns (each of which represents a
    [field](#field-database) or [variable](#variable-data)).

Tibble:
:   A modern replacement for R's data frame, which stores tabular data in columns
    and rows, defined and used in the [tidyverse](#tidyverse).

Tidy data:
:   Tabular data that satisfies [three conditions][tidy-data] that facilitate
    initial cleaning, and later exploration and analysis: (1) each variable
    forms a column, (2) each observation forms a row, and (3) each type of
    observation unit forms a table.  See also [table](#table).

tidymodels:
:   A collection of R packages for modeling and statistical analysis designed with
    a [shared philosophy][tidymodels].

Tidyverse:
:   A collection of R packages for operating on tabular data in consistent ways.

Truthy:
:   A truly Orwellian neologism meaning "not equivalent to false". See also
    [falsy](#falsy), but only if you are able to set aside your respect for the
    English language.

Type coercion:
:   FIXME

<h2 id="U">U</h2>

{:auto_ids}
Unicode:
:   A standard that defines numeric codes for many thousands of characters and
    symbols. Unicode does not define how those numbers are stored; that is done
    by standards like [UTF-8](#utf-8).

Unit test:
:   A test that exercises one property or expected behavior of a system.

Upstream repository:
:   FIXME

UTF-8:
:   A way to store the numeric codes representing Unicode characters in memory
    that is [backward-compatible](#backward-compatible) with the older [ASCII](#ascii) standard.

<h2 id="V">V</h2>

{:auto_ids}
Variable (program):
:   A name in a program that has some data associated with it. A variable's value
    can be changed after definition. See also [constant](#constant).

Variable (data):
:   FIXME

Variable arguments:
:   In a function, the ability to take any number of arguments.  R uses `...` to
    capture the "extra" arguments.

Vector:
:   A sequence of values, usually of [homogeneous](#homogeneous) type.  Vectors are the
    fundamental data structure in R; a [scalar](#scalar) is just a vector with exactly
    one element.

Vectorize:
:   To write code so that operations are performed on entire vectors, rather than
    element-by-element within loops.

Version control system:
:   A system for managing changes made to software during its development. See [Git](git).

Vignette:
:   A long-form guide used to provide details of a package beyond the README.md or
    function documentation.

<h2 id="W">W</h2>

{:auto_ids}
Whitespace:
:   The space, newline, carriage return, and horizontal and vertical tab
    characters that take up space but don't create a visible mark.  The name
    comes from their appearance on a printed page in the era of typewriters.

<h2 id="X">X</h2>

{:auto_ids}
XML:
:   A set of rules for defining HTML-like tags and using them to format documents
    (typically data). XML achieved license plate popularity in the early 2000s,
    but its complexity led many programmers to adopt [JSON](#json) instead.

<h2 id="Y">Y</h2>

{:auto_ids}
YAML:
:   FIXME

<h2 id="Z">Z</h2>

## Contributors

-   [Therese Anders](https://dornsife.usc.edu/anders)
-   [Marly Cormar](http://www.marlycormar.com/)
-   [Joyce Cahoon](https://jcahoon.netlify.com/)
-   [Daniel Chen](https://chendaniely.github.io)
-   [Dewey Dunnington](https://fishandwhistle.net/)
-   [Maya Gans](https://maya.rbind.io/)
-   [Leslie Huang](https://leslie-huang.github.io/)
-   [Greg Wilson](http://third-bit.com)

[re-doc]: https://stringr.tidyverse.org/articles/regular-expressions.html
[reprex]: https://github.com/tidyverse/reprex
[tidy-data]: https://vita.had.co.nz/papers/tidy-data.pdf
[tidymodels]: https://tidymodels.github.io/model-implementation-principles/index.html
