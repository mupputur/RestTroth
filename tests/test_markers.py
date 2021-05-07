import pytest
import sys
from common.fib_series import fib,rfib,foo,bar

def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(34) == 5702887

@pytest.mark.crazy
@pytest.mark.slow
def test_rfib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert rfib(34) == 5702887


"""
@pytest.mark.crazy
def test_foo():
    assert foo() == "foo"


@pytest.mark.crazy
def test_bar():
    assert bar() == "bar"

"""
@pytest.mark.skipif(
    sys.version_info[0] == 3 and sys.version_info[1] == 6,
    reason="Python version has to be higher than 3.5!")
def test_foo():
    assert foo() == "foo"

@pytest.mark.crazy
def test_bar():
    assert bar() == "bar"

@pytest.mark.parametrize(
    'n, res', [(0, 0),
               (1, 1),
               (2, 1),
               (3, 2),
               (4, 3),
               (5, 5),
               (6, 8)])
def test_fib(n, res):
    assert fib(n) == res

