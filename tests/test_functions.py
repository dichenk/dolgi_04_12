from dolzhnik_04_12.functions import get_val
from dolzhnik_04_12.functions import set_

def test_get_val():
    assert get_val({'hello': 'world'}, 'hello') == 'world'

def test_get_val_empty():
    assert get_val('') == 'dadibdabdabda'

def test_get_val_none():
    assert get_val(None) == 'dadibdabdabda'

def test_set_():
    assert set_({'a': {'b': {'c': 3}}}, ['a', 'b', 'c'], 4) == {'a': {'b': {'c': 4}}}

def test_set__none():
    assert set_(None, None, None) == "Error"

def test_set__another():
    assert set_(1, 2, 3, 4, 5) == "Error"

