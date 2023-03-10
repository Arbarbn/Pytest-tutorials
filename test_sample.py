import pytest

def inc(x):
    return x+1

def test_answer():
    assert inc(3) == 4
    
def test_file1_method():
    x = 5
    y = 6
    assert x+1 == y, "test failed"



