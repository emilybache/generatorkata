import pytest
import generatorkata

def test_simple_generator():
    g_it = generatorkata.simple_generator()

    # Verify
    assert next(g_it) == 1

    # The generator shall raise StopIteration when it reaches the end of its code
    with pytest.raises(StopIteration):
        next(g_it)