import math_func
import pytest

def test_add_strings():
    result = math_func.add('Hello ', 'Mihail')
    assert result == 'Hello Mihail'
    assert type(result) == str
    assert 'Heljs' not in result

def test_product_string():
    result = math_func.product('Hello ')
    assert result == 'Hello Mihail'
    assert type(result) == str
    assert 'Hello' in result


def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(8) == 10
    assert math_func.add(5, 5) == 10


def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(8) == 10
    assert math_func.add(5, 5) == 10

