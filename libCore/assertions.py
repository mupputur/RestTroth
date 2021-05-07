import pytest

"""
assert <condition>,optional<optional-message>
"""


def assert_true(resp, message=None):
    assert True == resp, message


def assert_false(resp, message=None):
    assert False == resp, message


def assert_equal(exp, act, message=None):
    assert exp == act, message
