from my_functions import (
    add,
    subtract,
    multiply,
    divide,
    is_even,
    is_odd,
    max_number,
    min_number,
    reverse_string,
    to_upper
)

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(2, 4) == 8

def test_divide():
    assert divide(10, 2) == 5

def test_is_even():
    assert is_even(4) is True

def test_is_odd():
    assert is_odd(5) is True

def test_max_number():
    assert max_number(10, 5) == 10

def test_min_number():
    assert min_number(10, 5) == 5

def test_reverse_string():
    assert reverse_string("hola") == "aloh"

def test_to_upper():
    assert to_upper("hola") == "HOLA"

#pytest test_functions.py
#coverage run -m pytest test_functions.py
#coverage report
#coverage html
