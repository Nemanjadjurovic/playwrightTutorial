Running Tests:
To run all tests in the current directory and its subdirectories, use:
pytest

You can also specify a specific module to run tests from:
`pytest test_mod.py`

To run tests in a directory:
`pytest testing/`

Selecting Tests:
By Keyword Expressions:
Run tests that match a given string expression (case-insensitive). You can use Python operators for filenames, class names, and function names:
`pytest -k "MyClass and not method"`

By Node IDs:
Each collected test has a unique node ID, which includes module filenames, class names, function names, and parameters from parametrization:
`pytest test_mod.py::test_func`

By Marker Expressions:
Run tests decorated with a specific marker (e.g., @pytest.mark.slow):
`pytest -m slow`

Stopping After Failures:
To stop after the first failure:
`pytest -x`

To stop after a specific number of failures (e.g., 2):
`pytest --maxfail=2`

Getting Help:
Show pytest version:
`pytest --version`

Show available built-in function arguments (fixtures):
`pytest --fixtures`

Show help on command-line and config file options:
pytest -h | --help

Modifying Traceback Printing:
Customize traceback format:
`pytest --tb=auto  # Default: 'long' for first and last entry, 'short' for others
pytest --tb=long  # Exhaustive, informative traceback
pytest --tb=short  # Shorter traceback format
pytest --tb=line  # One line per failure
pytest --tb=native  # Python standard library formatting
pytest --tb=no  # No traceback at all`