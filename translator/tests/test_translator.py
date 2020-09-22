"""
Unit and regression test for the translator package.
"""

# Import package, test suite, and other packages as needed
import translator
import pytest
import sys

def test_translator_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "translator" in sys.modules
