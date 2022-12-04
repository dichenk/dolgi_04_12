from dolzhnik_04_12.functions import get_val

def test_get_val():
    assert get_val({'hello': 'world'}, hello) == 'world'

def test_get_val_empty():
    assert get_val('') == 'dadibdabdabda'

def test_get_val_none():
    assert get_val(None) == 'dadibdabdabda'

def test_get_val_lot_of_arguments():
    assert get_val(1, 2, 3, 4, 5) == 'dadibdabdabda'
