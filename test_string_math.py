import math_func


def test_add_strings():
    result = math_func.add('Hello ', 'Mihail')
    assert result == 'Hello Mihail'
    assert type(result) == str
    assert 'Heljs' not in result

def test_product_string():
    result = math_func.product('Hello ')
    assert result == 'Hello Mihail'
