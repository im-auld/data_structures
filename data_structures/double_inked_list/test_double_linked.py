import pytest
from data_structures.double_inked_list import Node, DoubleLinkedList


@pytest.fixture(scope='session')
def empty():
    return DoubleLinkedList()


def test_node():
    """ Test node creation """
    node = Node(1)
    assert node.value == 1
    assert node.prev is None
    assert node.next is None


def test_double_linked_list():
    """ Test list creation and insert method """
    l = DoubleLinkedList()
    assert l.head is None
    assert l.tail is None
    assert l.size() == 0


def test_append():
    """ Test append method """
    l = DoubleLinkedList()
    l.append(1)
    assert l.tail.value == 1
    assert l.tail.next is None
    assert l.head.value == 1
    assert l.size() == 1
    l.append(2)
    assert l.tail.value == 2
    assert l.tail.next is None
    assert l.head.value == 1
    assert l.head.next.value == 2
    assert l.size() == 2


def test_pop_empty(empty):
    """ Test the pop method """
    with pytest.raises(LookupError):
        empty.pop()


def test_pop():
    """ Test the pop method """
    l = DoubleLinkedList()
    for i in range(1, 4):
        l.append(i)
    assert l.size() == 3
    assert l.pop() == 1
    assert l.head.value == 2
    assert l.tail.value == 3
    assert l.size() == 2
    assert l.pop() == 2
    assert l.head.value == 3
    assert l.tail.value == 3
    assert l.size() == 1


def test_shift_empty(empty):
    with pytest.raises(LookupError):
        empty.shift()


def test_shift():
    """ Test shift """
    l = DoubleLinkedList()
    for i in range(1, 4):
        l.append(i)
    assert l.size() == 3
    assert l.shift() == 3
    assert l.head.value == 1
    assert l.tail.value == 2
    assert l.size() == 2
    assert l.shift() == 2
    assert l.head.value == 1
    assert l.tail.value == 1
    assert l.size() == 1


def test_remove_empty(empty):
    with pytest.raises(LookupError):
        empty.remove(1)


def test_remove():
    """ Test remove """
    l = DoubleLinkedList()
    for i in range(1, 4):
        l.append(i)
    assert l.remove(2)
    assert l.head.value == 1
    assert l.head.next.value == 3
    assert l.tail.value == 3
    assert l.size() == 2
