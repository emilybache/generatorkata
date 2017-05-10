import pytest
from generatorkata import *

def test_simple_generator():
    g_it = simple_generator()

    # Verify
    assert next(g_it) == 1

    # The generator shall raise StopIteration when it reaches the end of its code
    with pytest.raises(StopIteration):
        next(g_it)

def test_clean_phonenumber():
    assert clean_phonenumber("0394 012-5-02") == "0394012502"

def test_cleaning_generator():
    data = """\
Silas Scarth,0394 012-5-02
Micheal Veronesi,01725 30 75
Blythe Milby,0027360 8 81
"""
    cg = cleaning_generator(data.splitlines())
    assert next(cg) == "Silas Scarth,0394012502"
    assert next(cg) == "Micheal Veronesi,017253075"
    assert next(cg) == "Blythe Milby,0027360881"
    with pytest.raises(StopIteration):
        next(cg)

def test_b_names_generator():
    data = """\
Adena Helble,0163 2783782
Elda Keough,0560397-05-82
"""
    bg = b_names_generator(data.splitlines())
    assert next(bg) == ("Adena Helble","0163 2783782")
    with pytest.raises(StopIteration):
        next(bg)

def test_clean_in_line():
    name = "Adena Helble"
    number = "0163 2783782"
    assert clean_phone_in_line( (name, number) ) == (name, "01632783782")

def test_cleaning_and_b_generator():
    data = """\
Silas Scarth,0394 012-5-02
Micheal Veronesi,01725 30 75
Blythe Milby,0027360 8 81
"""
    cg = map(clean_phone_in_line, b_names_generator(data.splitlines()))
    assert list(cg) == [("Blythe Milby", "0027360881")]



