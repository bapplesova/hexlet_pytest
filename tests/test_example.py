from hexlet_pytest.example import reverse


def test_reverse():
    assert reverse('Hexlet') == 'telxeH'


def test_reverse_for_empty_strung():
    assert reverse('') == ''


def test_emptiness():
    stack = []
    assert not stack
    stack.append('one')
    assert bool(stack)  # not not stack

    stack.pop()
    assert not stack


import pytest

def test_pop_with_empty_stack():
    stack = []
    with pytest.raises(IndexError):
        stack.pop()


