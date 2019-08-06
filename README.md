# glossRy

A small glossary of terms used in R and data science, designed for novices who
are still orienting themselves.  Contributions are very welcome: please see [the
contribution guidelines](CONTRIBUTING.md) if you would like to lend and hand,
and please note that all contributors must abide by our [Code of
Conduct](CONDUCT.md).

## Definitions

**Absolute path**: A path that points to the same location in the filesystem
  regardless of where it's evaluated. An absolute path is the equivalent of
  latitude and longitude in geography. See also **relative path**.

**Absolute row number**: the sequential index of a row in a table, regardless of
  what sections of the table is being displayed.

**Aggregation**: to combine many values into one, e.g., by summing a set of
  numbers or concatenating a set of strings.

**Aggregation function**: A function that combines many values into one, such as
  `sum` or `max`.

**Alias**: to have two or more references to the same physical data.

**Anonymous function**: a function that has not been assigned a name.  Anonymous
  functions are usually quite short, and are usually defined where they are
  used, e.g., as callbacks.

**Attribute**: a name-value pair associated with an object, used to store
  metadata about the object such as an array's dimensions.

**Base R**: FIXME

**Call stack**: A data structure that stores information about the active
  subroutines executed. `cst()` is a useful function provided in the `lobstr`
  package to visualize a call stack.

**Binary**: FIXME

**Branch**: A snapshot of a version of a Git repository. Multiple branches can
  capture multiple versions of the same repository. A **feature** branch captures
  the version of a repository that is under development and/or implements a new
  feature or correction. A **master** branch is the snapshot of the main version
  of a repository. See also **fork**.

**Cascading Style Sheets**: A way to describe how HTML should be rendered.

**Catch** (an exception): to accept responsibility for handling an error or
  other unexpected event.  R prefers **handling** a **condition** to "catching an
  exception".

**Character encoding**: A specification of how characters are stored as
  bytes. The most commonly-used encoding today is **UTF-8**.

**Closure**: A set of variables defined in the same **scope** whose existence has
  been preserved after that scope has ended. Closures are one of the trickiest
  ideas in programming.

**Comma-Separated Values**: A text format for tabular data in which each record
  is one row and fields are separated by commas. There are many minor
  variations, particularly around quoting of strings.

**Condition**: an error or other unexpected event that disrupts the normal flow
  of control.  See also **handle**.

**Constructor** (of a class): a function that creates an object of a particular
  class.  In the **S3** object system, constructors are a convention rather than a
  requirement.

**Copy-on-modify**: the practice of creating a new copy of aliased** data
  **whenever there is an attempt to modify it so that each reference will believe
  **theirs is the only one.

**Data frame**: FIXME

**Double square brackets**: an index enclosed in `[[...]]`, used to return a
  single value of the underlying type.  See also **single square brackets**.

**Empty vector**: a vector that contains no elements.  Empty vectors have a type
  such as logical or character, and are **not** the same as **null**.

**Data frame**: A class of objects that represents data and are typically used
  in fitting models.

**Docker**: FIXME. 

**Environment**: a structure that stores a set of variable names and the values
  they refer to.

**Escape sequence**: A sequence of characters used to represent some other
  character that would otherwise have a special meaning. For example, the escape
  sequence `\"` is used to represent a double-quote character inside a
  double-quoted string.

**Evaluation**: the process of taking a complex expression such as `1+2**3/4` and
  turning it into a single irreducible value.

**Exception**: An object that stores information about an error or other unusual
  event in a program. One part of a program will create and **throw** an exception
  to signal that something unexpected has happened; another part will **catch**
  it.

**Falsy**: A horrible neologism meaning "equivalent to false". See also the
  equally horrible **truthy**.
  
**Fork**: A copy of one person's Git repository that lives in another person's
  GitHub account. Changes to the content of a fork can be submitted to the
  **upstream** repository via a **pull request**. See also **branch**.

**Filter**: to choose a set of records according to the values they contain.

**Fully qualified name**: an unambiguous name of the form `package::thing`.

**Functional programming**: A style of programming in which data is transformed
  through successive application of functions, rather than by using control
  structures such as loops. Functional programming in R relies heavily on
  **higher-order functions**.

**Generic function**: a collection of functions with similar purpose, each
  operating on a different class of data.

**Global environment**: the **environment** that holds top-level definitions in R,
  e.g., those written directly in the interpreter.

**Global installation**: Installing a package in a location where it can be

**Git** A version control tool to record and manage changes to a project.

**GitHub**: a cloud-based platform built around **Git** that allows you to save
  versions of your project online and collaborate with other Git users.

**Global installation**: Installing a package in a location where it can be
  accessed by all users and projects. See also **local installation**.

**Global variable**: A variable defined outside any particular function, which
  is therefore visible to all functions. See also **local variable**.

**Group**: to divide data into subsets according to some criteria while leaving
  records in a single structure.

**GNU Public License**: A license that allows people to re-use software as long
  as they distribute the source of their changes.

**Handle** (a condition): to accept responsibility for handling an error or
  other unexpected event.  R prefers **handling a condition** to "catching an
  exception".

**Header row**: If present, the first of a **CSV** file that defines column names
  (but tragically, not their data types or units).

**Heterogeneous**: Having mixed type. For example, an **array** is said to be
  heterogeneous if it contains a mix of numbers, character strings, and values
  of other types. See also **homogeneous**.

**Higher-order function**: A function that operates on other functions. For
  example, the higher-order function `map` executes a given function once on
  each value in an **list**. Higher-order functions are heavily used in
  **functional programming**.

**Homogeneous**: Having a single type. For example, an **array** is said to be
  homogeneous if it contains only numbers or only character strings, but not a
  mix of the two.

**Hubris**: excessive pride or self-confidence.  See also **unit test** (lack of).

**Integrated Development Environment** (IDE): FIXME

**JSON**: A way to represent data by combining basic values like numbers and
  character strings in **arrays** and name/value structures. The acronym stands
  for "JavaScript Object Notation"; unlike better-defined standards like **XML**,
  it is unencumbered by a syntax for comments or ways to define **schemas**.

**Lazy evaluation**: delaying evaluation of an expression until the value is
  actually needed (or at least until after the point where it is first
  encountered).

**List**: a **vector** that can contain values of many different types.

**Local installation**: Placing a package inside a particular project so that it
  is only accessible within that project. See also **global installation**.

**Local variable**: A variable defined inside a function which is only visible
  within that function. See also **global variable** and **closure**.

**Logical indexing**: to index a vector or other structure with a vector of
  Booleans, keeping only the values that correspond to true values.

**Method**: an implementation of a **generic function** that handles objects of a
  specific class.

**MIT License**: A license that allows people to re-use software with no
  restrictions.

**Mutation**: Changing data in place, such as modifying an element of an array
  or adding a record to a database.

**NA**: a special value used to represent data that is Not Available.

**Name collision**: The ambiguity that arises when two or more things in a

**name collision**: The ambiguity that arises when two or more things in a
  program that have the same name are active at the same time. The **call stack**
  and **fully-qualified names** were invented in part to solve this problem.

**Negative selection**: to specify the elements of a vector or other data
  structure that **aren't** desired by negating their indices.

**Non-standard evaluation**: see **lazy evaluation**.

**NoSQL database**: Any database that doesn't use the **relational** model.  The
  awkward name comes from the fact that such databases don't use **SQL** as a
  query language.

**Null**: a special value used to represent a missing object.  `NULL` is not the
  same as `NA`, and neither is the same as an **empty vector**.

**Package**: a collection of code, data, and documentation that can be
  distributed and re-used.

**Package manager**: A program that does its best to keep track of the bits and
  bobs of software installed on a computer.

**Parameter**: A variable whose value is passed into a function when the
  function is called. Some writers distinguish parameters (the variables) from
  **arguments** (the values passed in), but others use the terms in the opposite
  sense. It's all very confusing.

**Parse**: To translate the text of a program or web page into a data structure
  in memory that the program can then manipulate.

**Pipe operator**: the `%>%` used to make the output of one function the input
  of the next.

**Prefix operator**: FIXME

**Production code**: Software that is delivered to an end user. The term is used
  to distinguish such code from test code, deployment infrastructure, and
  everything else that programmers write along the way.

**Pseudo-random number**: A value generated in a repeatable way that has the
  properties of being truly random.

**Pseudo-random number generator**: A function that can generate a series of
  **pseudo-random numbers** after being initialized with a **seed**.
  
**Pull request**: The request to merge a new feature or correction created on a
  user's fork of a git repository into the developer's main branch of the git
  repository. The developer will be notified of the change, review it, make or
  suggest changes, and potentially merge it. See also **fork**.

**Pull indexing**: vectorized indexing in which the value at location **i** in the
  index vector specifies which element of the source vector is being pulled into
  that location in the result vector, i.e., `result[i] = source[index[i]]`.  See
  also **push indexing**.

**Push indexing**: vectorized indexing in which the value at location **i** in the
  index vector specifies an element of the result vector that gets the
  corresponding element of the source vector, i.e., `result[index[i]] =
  source[i]`.  Push indexing can easily produce gaps and collisions.  See also
  **pull indexing**.

**Quosure**: a data structure containing an unevaluated expression and its
  environment.

**Quoting function**: a function that is passed expressions rather than the
  values of those expressions.

**Pull request**: A way to tell others about changes you have made to a GitHub
  repository. A few functions that can aid in your package development workflow
  are provided in the [usethis](https://usethis.r-lib.org/reference/pr_init.html) package.

**R hub**: A free platform available to check a `R` package on several
  different platforms in preparation for the CRAN submission process.

**R Markdown**: FIXME

**Raise**: To signal that something unexpected or unusual has happened in a
  program by creating an **exception** and handing it to the error-handling
  system, which then tries to find a point in the program that will **catch** it.

**Read-evaluate-print loop** (REPL): An interactive program that reads a command
  typed in by a user, executes it, prints the result, and then waits patiently
  for the next command. REPLs are often used to explore new ideas or for
  debugging.

**Recycle**: to re-use values from a shorter vector in order to generate a
  sequence of the same length as a longer one.

**Regular expression**: A pattern for matching text, written as text
  itself. Regular expressions are sometimes called "regexp", "regex", or "RE",
  and are as powerful as they are cryptic.  See [this documentation][re-doc]
  for more details.

**Relational database**: A database that organizes information into **tables**,
  each of which has a fixed set of named **fields** (shown as columns) and a
  variable number of **records** (shown as rows). See also **SQL**.

**Relative path**: A path whose destination is interpreted relative to some
  other location, such as the current directory. A relative path is the
  equivalent of giving directions using terms like "straight" and "left". See
  also **absolute path**.
  
**Reprex**: A reproducible example. When asking questions about coding problems
  online or filing issues on GitHub, you should always include a **reprex** so
  others can reproduce your problem and help. The
  [reprex](https://github.com/tidyverse/reprex) package can help!

**Relative row number**: the index of a row in a displayed portion of a table,
  which may or may not be the same as the **absolut row number** within the table.

**Repository**: FIXME

**Root directory**: The directory that contains everything else, directly or
  indirectly. The root directory is written `/` (a bare forward slash).

**S**: A language originally developed in Bell Labs for data analysis,
  statistical modeling, and graphics. R is a dialect of S.

**S3**: a framework for object-oriented programming in R.

**Scalar**: a single value of a particular type, such as 1 or "a".  Scalars
  don't really exist in R; values that appear to be scalars are actually vectors
  of unit length.

**Scalar**: FIXME

**Scope**: The portion of a program within which a definition can be seen and
  used. See **global-variable**, **local-variable**, and **closure**.

**Script**: FIXME

**Seed**: A value used to initialize a **pseudo-random number generator**.

**Select**: to choose entire columns from a table by name or location.

**Signal** (a condition): a way of indicating that something has gone wrong in a
  program, or that some other unexpected event has occurred.  R prefers
  **signalling** a **condition** to "raising an exception".

**Single square brackets**: an index enclosed in `[...]`, used to select a
  structure from another structure.  See also **double square brackets**.

**singleton**: A set whose cardinality is 1.

**SQL**: The language used for writing queries for **relational databases**. The
  term was originally an acronym for Structured Query Language.

**String**: A block of text in a program. The term is short for "character
  string".

**String interpolation**: The process of inserting text corresponding to
  specified values into a string, usually to make output human-readable.

**Table**: A set of uniformly-formatted **records** in a **relational database**.
  Tables are usually drawn with rows (each of which represents one record) and
  columns (each of which represents a **field**).

**Tibble**: a modern replacement for R's data frame, which stores tabular data
  in columns and rows, defined and used in the **tidyverse**.

**Tidy data**: Tabular data that satisfies
  [three conditions](https://vita.had.co.nz/papers/tidy-data.pdf)
  that facilitate initial cleaning, and later exploration and analysis:

1.  Each variable forms a column.
2.  Each observation forms a row.
3.  Each type of observation unit forms a table.


**tidymodels**: A collection of modeling packages designed with a
  [shared philosophy](https://tidymodels.github.io/model-implementation-principles/index.html).

**Tidyverse**: a collection of R packages for operating on tabular data in
  consistent ways.

**Tidymodels**: a collection of R packages for modeling and statistical
analysis.

**Truthy**: A truly Orwellian neologism meaning "not equivalent to false". See
  also **falsy**, but only if you are able to set aside your respect for the
  English language.

**Unicode**: A standard that defines numeric codes for many thousands of
  characters and symbols. Unicode does not define how those numbers are stored;
  that is done by standards like **UTF-8**.

**Unit test**: A test that exercises one property or expected behavior of a
  system.

**UTF-8**: A way to store the numeric codes representing Unicode characters in
  memory that is **backward-compatible** with the older **ASCII** standard.

**Variable**: A name in a program that has some data associated with it. A
  variable's value can be changed after definition. See also **constant**.

**Variable arguments**: in a function, the ability to take any number of
  arguments.  R uses `...` to capture the "extra" arguments.

**Vector**: a sequence of values, usually of homogeneous** type.  Vectors are the
  fundamental data structure in R; **scalars** are actually vectors of unit
  length.

**Vectorize**: to write code so that operations are performed on entire vectors,
  rather than element-by-element within loops.

**Vignette**: a long-form guide used to provide details of a package beyond
the README.md or function documentation.

**Whitespace**: The space, newline, carriage return, and horizontal and vertical
  tab characters that take up space but don't create a visible mark.  The name
  comes from their appearance on a printed page in the era of typewriters.

## Contributors

-   [Therese Anders](https://dornsife.usc.edu/anders)
-   [Marly Cormar](http://www.marlycormar.com/)
-   [Joyce Cahoon](https://jcahoon.netlify.com/)
-   [Greg Wilson](http://third-bit.com)

[re-doc]: https://stringr.tidyverse.org/articles/regular-expressions.html
