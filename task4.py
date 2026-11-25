"""Flatten arbitrarily nested lists using a generator."""

import types


def flat_generator(list_of_list):
    """Yield non-list elements using a stack of iterators."""
    stack = [iter(list_of_list)]

    while stack:
        try:
            item = next(stack[-1])
        except StopIteration:
            stack.pop()
            continue

        if isinstance(item, list):
            stack.append(iter(item))
        else:
            yield item


def test_4():
    """Check nested lists, deep nesting and generator type."""
    data = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []],
    ]
    expected = ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    for item, expected_item in zip(flat_generator(data), expected):
        assert item == expected_item

    assert list(flat_generator(data)) == expected
    assert isinstance(flat_generator(data), types.GeneratorType)

    assert list(flat_generator([[], [[]], 'Python', False, None])) == [
        'Python', False, None
    ]
    assert list(flat_generator([])) == []

    deep = [42]
    for _ in range(2000):
        deep = [deep]

    assert list(flat_generator(deep)) == [42]


if __name__ == '__main__':
    test_4()
    print('Задание 4: все проверки пройдены')