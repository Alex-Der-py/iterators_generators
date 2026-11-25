"""Flatten a list of lists using an iterator."""


class FlatIterator:
    """Iterate over the elements of a two-level list."""

    def __init__(self, list_of_list):
        """Create outer and inner iterators."""
        self.outer_iterator = iter(list_of_list)
        self.inner_iterator = iter([])

    def __iter__(self):
        """Return the iterator itself."""
        return self

    def __next__(self):
        """Return the next element or raise StopIteration."""
        while True:
            try:
                return next(self.inner_iterator)
            except StopIteration:
                self.inner_iterator = iter(next(self.outer_iterator))


def test_1():
    """Check order, empty lists and iterator exhaustion."""
    data = [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]]
    expected = ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    for item, expected_item in zip(FlatIterator(data), expected):
        assert item == expected_item

    assert list(FlatIterator(data)) == expected

    assert list(FlatIterator([[], [0, False], [], [None], []])) == [
        0, False, None
    ]
    assert list(FlatIterator([])) == []

    iterator = FlatIterator([[1, 2]])
    assert iter(iterator) is iterator
    assert next(iterator) == 1
    assert list(iterator) == [2]
    assert next(iterator, 'end') == 'end'


if __name__ == '__main__':
    test_1()
    print('Задание 1: все проверки пройдены')