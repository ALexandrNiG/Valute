import pytest

from logo_game import generate_unique_numbers

# tests for: generate_unique_numbers

testlencount = 80
testminbound = 0
testmaxbound = 100


def test_lencorrect():
    valid = generate_unique_numbers(testlencount, testminbound, testmaxbound)
    assert len(valid) == testlencount


def test_correctvalues():
    valid = generate_unique_numbers(testlencount, testminbound, testmaxbound)
    for item in valid:
        assert (testminbound <= item <= testmaxbound)


def test_uniquevalues():
    valid = generate_unique_numbers(testlencount, testminbound, testmaxbound)
    assert len(set(valid)) == testlencount


def test_maxpossiblecount():
    maxpossiblelen = 101
    valid = generate_unique_numbers(maxpossiblelen, testminbound, testmaxbound)
    assert len(valid) == maxpossiblelen


def test_lenoutside():
    impossiblelen = 102
    with pytest.raises(ValueError):
        generate_unique_numbers(impossiblelen, testminbound, testmaxbound)


def test_countzero_resultempty():
    assert len(generate_unique_numbers(0, testminbound, testmaxbound)) == 0


def test_maxlessthanmin_raises():
    with pytest.raises(ValueError):
        generate_unique_numbers(100, 2000, 1500)