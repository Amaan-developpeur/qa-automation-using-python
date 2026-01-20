# ----------------------------------
# Marker: A marker is a label you attach to a test.
# Pytest reads markers → decides what to run / skip / expect
# ---------------------------------------------

# --------------------------
# Core Syntax Patterns

# 1. Simple Marker: A simple marker is just a label attached to a test.

# import pytest

# @pytest.mark.smoke
# def test_login():
#     assert 1 == 1

# MULTIPLE SIMPLE MARKERS ON ONE TEST
# @pytest.mark.smoke
# @pytest.mark.regression
# def test_payment():
#     assert 2 + 2 == 4

# Running Tests
# pytest -m smoke
# pytest -m regression

# pytest -m "smoke and not slow"

# A marker never affects test logic.
# It only affects which tests run.

# Marker with arguements: 
# A marker with arguments is still a marker,
# but now it carries extra information.

# Purpose: To answer why or when a marker is applied.

# @pytest.mark.skip(reason="Feature under development")
# def test_payment():
#     assert 1 == 1

import sys

# @pytest.mark.skipif(sys.platform == "win32", reason="Linux only")
# def test_linux_feature():
#     assert True

# | Marker      | Runs Test?             | Purpose                 |
# | ----------- | ---------------------- | ----------------------- |
# | skip        | No                   | Disable test            |
# | skipif      | Conditional          | Disable under condition |
# | xfail       | Yes                 | Known failure           |
# | parametrize | Yes (multiple times) | Multiple inputs         |

# MARKER DISCIPLINE (THIS MATTERS MORE THAN SYNTAX)
# Rule 1 — Every marker must be declared

# No exceptions.

# If it’s used in code → it belongs in pytest.ini.

# Rule 2 — Few markers > many markers

# Bad:

# @pytest.mark.login
# @pytest.mark.payment
# @pytest.mark.critical
# @pytest.mark.fast


# Good:

# @pytest.mark.smoke
# @pytest.mark.regression


# Markers are categories, not descriptions.

# Rule 3 — Don’t lie with markers

#  Marking everything as smoke
#  Using skip to hide failures
#  Leaving xfail forever








