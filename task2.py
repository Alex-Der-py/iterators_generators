"""Flatten a list of lists using a generator."""

import types


def flat_generator(list_of_lists):
    """Yield individual elements of each inner list."""
    for inner_list in list_of_lists:
        for item in inner_list:
            yield item


def test_2():
    """Check order, empty lists and generator type."""
    data = [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]]
    expected = ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    for item, expected_item in zip(flat_generator(data), expected):
        assert item == expected_item

    assert list(flat_generator(data)) == expected
    assert isinstance(flat_generator(data), types.GeneratorType)

    assert list(flat_generator([[], [0, False], [], [None], []])) == [
        0, False, None
    ]
    assert list(flat_generator([])) == []


if __name__ == '__main__':
    test_2()
    print('Задание 2: все проверки пройдены')
