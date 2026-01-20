# QA Automation Journey

This repository documents my hands-on journey from Python testing fundamentals to building a structured QA automation framework using Pytest.

The focus is not just on writing tests, but on understanding:
- test discovery
- imports and project structure
- fixtures and scopes
- markers and selective execution
- framework-level best practices

## Folder Structure
```
C:.
│   pytest.ini
│
├───.pytest_cache
│   │   .gitignore
│   │   CACHEDIR.TAG
│   │   README.md
│   │
│   └───v
│       └───cache
│               lastfailed
│               nodeids
│               stepwise
│
├───basics
│       day1_basics.py
│       day2_data_driven.py
│       day3_negative_testing.py
│       day4_setup_teardown.py
│
├───day5_pytest
│   │   test_basic_pytest.py
│   │   test_fixtures.py
│   │
│   └───__pycache__
│           test_basic_pytest.cpython-313-pytest-8.3.4.pyc
│           test_fixtures.cpython-313-pytest-8.3.4.pyc
│
├───markers_pytest
│   │   markers.py
│   │   test_markers1.py
│   │
│   └───__pycache__
│           test_markers1.cpython-313-pytest-8.3.4.pyc
│
└───qa_framework
    │   __init__.py
    │
    ├───core
    │   │   auth.py
    │   │   calculator.py
    │   │   __init__.py
    │   │
    │   └───__pycache__
    │           calculator.cpython-313.pyc
    │           __init__.cpython-313.pyc
    │
    ├───tests
    │   │   conftest.py
    │   │   test_basic.py
    │   │   test_framework_fixtures.py
    │   │
    │   └───__pycache__
    │           conftest.cpython-313-pytest-8.3.4.pyc
    │           test_basic.cpython-313-pytest-8.3.4.pyc
    │           test_framework_fixtures.cpython-313-pytest-8.3.4.pyc
    │
    ├───utils
    └───__pycache__
            __init__.cpython-313.pyc


(base) C:\Users\DELL\OneDrive\Desktop\QA_Automation\learnings\qa_day1>
```
## Project Structure

### basics/
Covers Python testing fundamentals:
- basic assertions
- data-driven testing
- negative test scenarios
- setup and teardown concepts

### day5_pytest/
Introduction to Pytest core concepts:
- test discovery rules
- parametrization
- fixtures
- exception handling
- temporary resources

### markers_pytest/
Focuses on Pytest markers:
- defining custom markers
- tagging tests (e.g. regression)
- running selective test suites using `-m`

Example:
```bash
pytest -m regression
