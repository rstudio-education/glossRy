# glossRy

A small glossary of terms used in R and data science, designed for novices who
are still orienting themselves.  Contributions are very welcome (particularly
ones that fill in `FIXME` markers): please see [the contribution
guidelines](CONTRIBUTING.md) if you would like to lend and hand, and please note
that all contributors must abide by our [Code of Conduct](CONDUCT.md).

<a href="#A">A</a>
<a href="#B">B</a>
<a href="#C">C</a>
<a href="#D">D</a>
<a href="#E">E</a>
<a href="#F">F</a>
<a href="#G">G</a>
<a href="#H">H</a>
<a href="#I">I</a>
<a href="#J">J</a>
<a href="#K">K</a>
<a href="#L">L</a>
<a href="#M">M</a>
<a href="#N">N</a>
<a href="#O">O</a>
<a href="#P">P</a>
<a href="#Q">Q</a>
<a href="#R">R</a>
<a href="#S">S</a>
<a href="#T">T</a>
<a href="#U">U</a>
<a href="#V">V</a>
<a href="#W">W</a>
<a href="#X">X</a>
<a href="#Y">Y</a>
<a href="#Z">Z</a>

<h2 id="A">A</h2>

**Absolute path**: A path that points to the same location in the filesystem
  regardless of where it's evaluated. An absolute path is the equivalent of
  latitude and longitude in geography. See also **relative path**.

**Absolute row number**: The sequential index of a row in a table, regardless of
  what sections of the table is being displayed.

**Aggregation**: To combine many values into one, e.g., by summing a set of
  numbers or concatenating a set of strings.

**Aggregation function**: A function that combines many values into one, such as
  `sum` or `max`.

**Aliasing**: To have two or more references to the same physical data.

**Anonymous function**: A function that has not been assigned a name.  Anonymous
  functions are usually quite short, and are usually defined where they are
  used, e.g., as callbacks.

**Arguments**: The values passed into a function. Some authors use the term as
  a synonym for **parameter** and some do not; it's all very confusing.

**ASCII**: A standard way to represent the characters commonly used in the
  Western European languages as 7- or 8-bit integers, now superceded by
  **Unicode**.

**Attribute**: A name-value pair associated with an object, used to store
  metadata about the object such as an array's dimensions.

<h2 id="B">B</h2>

**Backward-compatible**: FIXME

**Base R**: FIXME

**Binary**: FIXME

**Binding**: FIXME

**Branch**: A snapshot of a version of a Git repository. Multiple branches can
  capture multiple versions of the same repository. See also **feature branch**,
  **fork**, and **master branch**.

<h2 id="C">C</h2>

**Call stack**: A data structure that stores information about the active
  subroutines executed. `cst()` is a useful function provided in the `lobstr`
  package to visualize a call stack.

**Cascading Style Sheets**: A way to describe how HTML should be rendered.

**Catch** (an exception): To accept responsibility for handling an error or
  other unexpected event.  R prefers "handling a condition" to "catching an
  exception".  See also **condition** and **handle**.

**Character encoding**: A specification of how characters are stored as
  bytes. The most commonly-used encoding today is **UTF-8**.

**Class**: FIXME

**Closure**: A set of variables defined in the same **scope** whose existence has
  been preserved after that scope has ended. Closures are one of the trickiest
  ideas in programming.

**Coercion**: see **type coercion**.

**Comma-Separated Values**: A text format for tabular data in which each record
  is one row and fields are separated by commas. There are many minor
  variations, particularly around quoting of strings.

**Condition**: An error or other unexpected event that disrupts the normal flow
  of control.  See also **handle**.

**Constant**: FIXME

**Constructor** (of a class): A function that creates an object of a particular
  class.  In the **S3** object system, constructors are a convention rather than a
  requirement.

**Copy-on-modify**: The practice of creating a new copy of aliased data
  whenever there is an attempt to modify it so that each reference will
  believe theirs is the only one.  See **aliasing**.

<h2 id="D">D</h2>

**Data frame**: FIXME

**Double square brackets**: An index enclosed in `[[...]]`, used to return a
  single value of the underlying type.  See also **single square brackets**.

**Data frame**: A class of objects that represents data and are typically used
  in fitting models.

**Docker**: FIXME.

**Double**: Short for "double-precision floating-point number", meaning a 64-bit
  numeric value with a fractional part and an exponent.

**Dynamic scoping**: FIXME.  See **lexical scoping**.

<h2 id="E">E</h2>

**Eager evaluation**: FIXME.  See also **lazy evaluation**.

**Empty vector**: A vector that contains no elements.  Empty vectors have a type
  such as logical or character, and are *not* the same as **null**.

**Environment**: A structure that stores a set of variable names and the values
  they refer to.

**Escape sequence**: A sequence of characters used to represent some other
  character that would otherwise have a special meaning. For example, the escape
  sequence `\"` is used to represent a double-quote character inside a
  double-quoted string.

**Evaluation**: The process of taking a complex expression such as `1+2*3/4` and
  turning it into a single irreducible value.

**Exception**: An object that stores information about an error or other unusual
  event in a program. One part of a program will create and **raise** an exception
  to signal that something unexpected has happened; another part will **catch**
  it.

<h2 id="F">F</h2>

**Falsy**: A horrible neologism meaning "equivalent to false". See also the
  equally horrible **truthy**.

**Feature branch**: FIXME

**Field** (in a database table): FIXME

**Fork**: A copy of one person's Git repository that lives in another person's
  GitHub account. Changes to the content of a fork can be submitted to the
  **upstream repository** via a **pull request**. See also **branch**.

**Filter**: To choose a set of records according to the values they contain.

**Fully-qualified name**: An unambiguous name of the form `package::thing`.

**Functional programming**: A style of programming in which data is transformed
  through successive application of functions, rather than by using control
  structures such as loops.  See also **higher-order function**.

<h2 id="G">G</h2>

**Generic function**: A collection of functions with similar purpose, each
  operating on a different class of data.

**Global environment**: The **environment** that holds top-level definitions in R,
  e.g., those written directly in the interpreter.

**Global installation**: Installing a package in a location where it can be

**Git** A version control tool to record and manage changes to a project.

**GitHub**: A cloud-based platform built around **Git** that allows you to save
  versions of your project online and collaborate with other Git users.

**Global installation**: Installing a package in a location where it can be
  accessed by all users and projects. See also **local installation**.

**Global variable**: A variable defined outside any particular function, which
  is therefore visible to all functions. See also **local variable**.

**Group**: To divide data into subsets according to some criteria while leaving
  records in a single structure.

**GNU Public License**: A license that allows people to re-use software as long
  as they distribute the source of their changes.

<h2 id="H">H</h2>

**Handle** (a condition): To accept responsibility for handling an error or
  other unexpected event.  R prefers "handling a condition" to "catching an
  exception".  See also **condition** and **exception**.

**Header row**: If present, the first of a CSV file that defines column names
  (but tragically, not their data types or units).  See also **comma-separated values**.

**Heterogeneous**: Having mixed type. For example, an list can contain a mix of
  numbers, character strings, and values of other types. See also
  **homogeneous**.

**Higher-order function**: A function that operates on other functions. For
  example, the higher-order function `map` executes a given function once on
  each value in an **list**. Higher-order functions are heavily used in
  **functional programming**.

**Homogeneous**: Having a single type. For example, a **vector** must be
  homogeneous: its values must all be numeric, logical, etc.

**Hubris**: Excessive pride or self-confidence.  See also **unit test** (lack of).

<h2 id="I">I</h2>

**Instance**: FIXME

**Integrated Development Environment** (IDE): FIXME

<h2 id="J">J</h2>

**JSON**: A way to represent data by combining basic values like numbers and
  character strings in lists and name/value structures. The acronym stands for
  "JavaScript Object Notation"; unlike better-defined standards like **XML**, it
  is unencumbered by a syntax for comments or ways to define a **schema**.

**Lazy evaluation**: Delaying evaluation of an expression until the value is
  actually needed (or at least until after the point where it is first
  encountered).

<h2 id="K">K</h2>

<h2 id="L">L</h2>

**Lexical scoping**: FIXME.  See **dynamic scoping**.

**List**: A **vector** that can contain values of many different types.

**Local installation**: Placing a package inside a particular project so that it
  is only accessible within that project. See also **global installation**.

**Local variable**: A variable defined inside a function which is only visible
  within that function. See also **global variable** and **closure**.

**Logical indexing**: To index a vector or other structure with a vector of
  Booleans, keeping only the values that correspond to true values.

<h2 id="M">M</h2>

**Master branch**: FIXME

**Merge** (in Git): FIXME

**Method**: An implementation of a **generic function** that handles objects of a
  specific class.

**MIT License**: A license that allows people to re-use software with no
  restrictions.

**Mutation**: Changing data in place, such as modifying an element of an array
  or adding a record to a database.

<h2 id="N">N</h2>

**NA**: A special value used to represent data that is Not Available.

**Name collision**: The ambiguity that arises when two or more things in a

**name collision**: The ambiguity that arises when two or more things in a
  program that have the same name are active at the same time. See also **call
  stack** and **fully-qualified name**.

**Negative selection**: To specify the elements of a vector or other data
  structure that aren't desired by negating their indices.

**Non-standard evaluation**: See **lazy evaluation**.

**NoSQL database**: Any database that doesn't use the relational model.  The
  awkward name comes from the fact that such databases don't use **SQL** as a
  query language.  See also **relational database**.

**Null**: A special value used to represent a missing object.  `NULL` is not the
  same as `NA`, and neither is the same as an **empty vector**.

<h2 id="O">O</h2>

**Observation**: FIXME

<h2 id="P">P</h2>

**Package**: A collection of code, data, and documentation that can be
  distributed and re-used.

**Package manager**: A program that does its best to keep track of the bits and
  bobs of software installed on a computer.

**Parameter**: A variable whose value is passed into a function when the
  function is called. Some writers distinguish parameters (the variables) from
  **arguments** (the values passed in), but others use the terms in the opposite
  sense. It's all very confusing.

**Parse**: To translate the text of a program or web page into a data structure
  in memory that the program can then manipulate.

**Pipe operator**: The `%>%` used to make the output of one function the input
  of the next.

**Prefix operator**: FIXME

**Production code**: Software that is delivered to an end user. The term is used
  to distinguish such code from test code, deployment infrastructure, and
  everything else that programmers write along the way.

**Pseudo-random numbers**: Value generated in a repeatable way that resemble the
  true randomness of the universe well enough to fool merely mortal observers.

**Pseudo-random number generator**: A function that can generate **pseudo-random
  numbers**.  See also **seed**.
  
**Pull request**: The request to merge a new feature or correction created on a
  user's fork of a Git repository into the **upstream repository**. The
  developer will be notified of the change, review it, make or suggest changes,
  and potentially merge it. See also **fork**.

**Pull indexing**: Vectorized indexing in which the value at location `i` in the
  index vector specifies which element of the source vector is being pulled into
  that location in the result vector, i.e., `result[i] = source[index[i]]`.  See
  also **push indexing**.

**Push indexing**: Vectorized indexing in which the value at location `i` in the
  index vector specifies an element of the result vector that gets the
  corresponding element of the source vector, i.e., `result[index[i]] =
  source[i]`.  Push indexing can easily produce gaps and collisions.  See also
  **pull indexing**.

<h2 id="Q">Q</h2>

**Quosure**: A data structure containing an unevaluated expression and its
  environment.

**Quoting function**: A function that is passed expressions rather than the
  values of those expressions.

<h2 id="R">R</h2>

**R hub**: A free platform available to check a `R` package on several
  different platforms in preparation for the CRAN submission process.

**R Markdown**: FIXME

**Raise**: To signal that something unexpected or unusual has happened in a
  program by creating an **exception** and handing it to the error-handling
  system, which then tries to find a point in the program that will **catch** it.

**Reactive programming**: A style of programming in which actions are triggered
  by external events.

**Reactive variable**: A variable whose value is automatically updated when some
  other value or values change.  Reactive variables are used extensively in
  **Shiny**.

**Read-evaluate-print loop** (REPL): An interactive program that reads a command
  typed in by a user, executes it, prints the result, and then waits patiently
  for the next command. REPLs are often used to explore new ideas or for
  debugging.

**Rebase** (in Git): FIXME

**Record** (in a database table): FIXME

**Recycle**: To re-use values from a shorter vector in order to generate a
  sequence of the same length as a longer one.

**Regular expression**: A pattern for matching text, written as text
  itself. Regular expressions are sometimes called "regexp", "regex", or "RE",
  and are as powerful as they are cryptic.  See [this documentation][re-doc]
  for more details.

**Relational database**: A database that organizes information into tables,
  each of which has a fixed set of named fields (shown as columns) and a
  variable number of records (shown as rows). See also **SQL**, **table**.

**Relative path**: A path whose destination is interpreted relative to some
  other location, such as the current directory. A relative path is the
  equivalent of giving directions using terms like "straight" and "left". See
  also **absolute path**.
  
**Reprex**: A reproducible example. When asking questions about coding problems
  online or filing issues on GitHub, you should always include a **reprex** so
  others can reproduce your problem and help. The [reprex][reprex] package can
  help!

**Relative row number**: The index of a row in a displayed portion of a table,
  which may or may not be the same as the **absolute row number** within the table.

**Repository**: FIXME

**Root directory**: The directory that contains everything else, directly or
  indirectly. The root directory is written `/` (a bare forward slash).

<h2 id="S">S</h2>

**S**: A language originally developed in Bell Labs for data analysis,
  statistical modeling, and graphics. R is a dialect of S.

**S3**: A framework for object-oriented programming in R.

**Sr**: A framework for object-oriented programming in R.

**Scalar**: A single value of a particular type, such as 1 or "a".  Scalars
  don't really exist in R; values that appear to be scalars are actually vectors
  of unit length.

**Scalar**: FIXME

**Schema**: A specification of the format of a dataset, including the name,
  format, and content of each **table**.

**Scope**: The portion of a program within which a definition can be seen and
  used. See  **closure**, **global variable**, and **local variable**.

**Script**: FIXME

**Seed**: A value used to initialize a **pseudo-random number generator**.

**Select**: To choose entire columns from a table by name or location.

**Shiny**: FIXME

**Signal** (a condition): A way of indicating that something has gone wrong in a
  program, or that some other unexpected event has occurred.  R prefers
  "signalling a condition" to "raising an exception".

**Single square brackets**: An index enclosed in `[...]`, used to select a
  structure from another structure.  See also **double square brackets**.

**Singleton**: A set with only one element, or a **class** with only one
  **instance**.

**SQL**: The language used for writing queries for a **relational
  database**. The term was originally an acronym for Structured Query Language.

**Squash** (in Git): FIXME

**Stack frame**: FIXME

**String**: A block of text in a program. The term is short for "character
  string".

**String interpolation**: The process of inserting text corresponding to
  specified values into a string, usually to make output human-readable.

<h2 id="T">T</h2>

**Table**: A set of records in a **relational database** or observations in a
  **data frame**.  Tables are usually displayed as rows (each of which
  represents one **record** or **observation**) and columns (each of which
  represents a **field** or **variable**).

**Tibble**: A modern replacement for R's data frame, which stores tabular data
  in columns and rows, defined and used in the **tidyverse**.

**Tidy data**: Tabular data that satisfies [three conditions][tidy-data] that
  facilitate initial cleaning, and later exploration and analysis: (1) each
  variable forms a column, (2) each observation forms a row, and (3) each type
  of observation unit forms a table.  See also **table**.

**tidymodels**: A collection of R packages for modeling and statistical analysis
  designed with a [shared philosophy][tidymodels].

**Tidyverse**: A collection of R packages for operating on tabular data in
  consistent ways.

**Truthy**: A truly Orwellian neologism meaning "not equivalent to false". See
  also **falsy**, but only if you are able to set aside your respect for the
  English language.

**Type coercion**: FIXME

<h2 id="U">U</h2>

**Unicode**: A standard that defines numeric codes for many thousands of
  characters and symbols. Unicode does not define how those numbers are stored;
  that is done by standards like **UTF-8**.

**Unit test**: A test that exercises one property or expected behavior of a
  system.

**Upstream repository**: FIXME

**UTF-8**: A way to store the numeric codes representing Unicode characters in
  memory that is **backward-compatible** with the older **ASCII** standard.

<h2 id="V">V</h2>

**Variable** (in a program): A name in a program that has some data associated
  with it. A variable's value can be changed after definition. See also
  **constant**.

**Variable** (in tabular data): FIXME

**Variable arguments**: In a function, the ability to take any number of
  arguments.  R uses `...` to capture the "extra" arguments.

**Vector**: A sequence of values, usually of **homogeneous** type.  Vectors are
  the fundamental data structure in R; a **scalar** is just a vector with
  exactly one element.

**Vectorize**: To write code so that operations are performed on entire vectors,
  rather than element-by-element within loops.

**Vignette**: A long-form guide used to provide details of a package beyond the
  README.md or function documentation.

<h2 id="W">W</h2>

**Whitespace**: The space, newline, carriage return, and horizontal and vertical
  tab characters that take up space but don't create a visible mark.  The name
  comes from their appearance on a printed page in the era of typewriters.

<h2 id="X">X</h2>

**XML**: A set of rules for defining HTML-like tags and using them to format
  documents (typically data). XML achieved license plate popularity in the early
  2000s, but its complexity led many programmers to adopt **JSON** instead.

<h2 id="Y">Y</h2>

<h2 id="Z">Z</h2>

## Contributors

-   [Therese Anders](https://dornsife.usc.edu/anders)
-   [Marly Cormar](http://www.marlycormar.com/)
-   [Joyce Cahoon](https://jcahoon.netlify.com/)
-   [Dewey Dunnington](https://fishandwhistle.net/)
-   [Maya Gans](https://maya.rbind.io/)
-   [Leslie Huang](https://leslie-huang.github.io/)
-   [Greg Wilson](http://third-bit.com)

[re-doc]: https://stringr.tidyverse.org/articles/regular-expressions.html
[reprex]: https://github.com/tidyverse/reprex
[tidy-data]: https://vita.had.co.nz/papers/tidy-data.pdf
[tidymodels]: https://tidymodels.github.io/model-implementation-principles/index.html
