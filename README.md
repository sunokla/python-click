span
====

This is the span application.

命令行方式的python项目工程.

Minimum Requirements
--------------------

-   Python 3.5+

Optional Requirements
---------------------

-   [pytest](http://pytest.org) (for running the test suite)
-   [Sphinx](http://sphinx-doc.org) (for generating documentation)

Basic Setup
-----------

Install for the current user:

``` {.sourceCode .console}
$ python -m pip install . --user
```

Run the application:

``` {.sourceCode .console}
$ python -m span --help
```

Run the test suite:

``` {.sourceCode .console}
$ pytest test/
```

Build documentation:

``` {.sourceCode .console}
$ sphinx-build -b html doc doc/_build/html
```
