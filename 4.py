import types
from collections import deque


def flat_generator(list_of_lists):
    list_of_lists = deque(list_of_lists)
    while list_of_lists:
        el = list_of_lists.popleft()
        if isinstance(el, list):
            for i in flat_generator(el):
                if not isinstance(i, list):
                    yield i
                else:
                    flat_generator(i)
        else:
            yield el


def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()