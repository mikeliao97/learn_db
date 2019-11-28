import uuid

import pytest

from .btree import Btree


@pytest.fixture()
def btree():
    tree = Btree(3)
    btree.insert(1)
    return tree



class TestBTree:
    def test_simple_insert(self, btree):
        assert False

    def test_delete(self, btree):
        assert False
