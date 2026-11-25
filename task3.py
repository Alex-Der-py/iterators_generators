"""Flatten arbitrarily nested lists using an iterator."""


class FlatIterator:
    """Iterate over nested lists using a stack."""

    def __init__(self, list_of_list):
        """Initialize the stack with the outer iterator."""
        self.stack = [iter(list_of_list)]

    def __iter__(self):
        """Return the iterator itself."""
        return self

    def __next__(self):
        """Return the next non-list element."""
        while self.stack:
            try:
                item = next(self.stack[-1])
            except StopIteration:
                self.stack.pop()
                continue

            if isinstance(item, list):
                self.stack.append(iter(item))
            else:
                return item

        raise StopIteration


def test_3():
    """Check nested lists, empty lists and deep nesting."""
    data = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []],
    ]
    expected = ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    for item, expected_item in zip(FlatIterator(data), expected):
        assert item == expected_item

    assert list(FlatIterator(data)) == expected

    assert list(FlatIterator([[], [[]], 'Python', False, None])) == [
        'Python', False, None
    ]
    assert list(FlatIterator([])) == []

    deep = [42]
    for _ in range(2000):
        deep = [deep]

    assert list(FlatIterator(deep)) == [42]


if __name__ == '__main__':
    test_3()
    print('Задание 3: все проверки пройдены')
