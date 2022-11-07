from collections import deque


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = deque(list_of_list)

    def __iter__(self):
        self._list = deque(self.list_of_list.popleft())
        return self

    def __next__(self):
        if not self.list_of_list and not self._list:
            raise StopIteration
        if not self._list:
            self._list = deque(self.list_of_list.popleft())
        return self._list.popleft()


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    test_1()