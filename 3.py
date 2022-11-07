from collections import deque


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = deque(list_of_list)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.list_of_list:
            raise StopIteration
        el = self.list_of_list[0]
        if isinstance(el, list):
            self.list_of_list.popleft()
            for i in el[::-1]:
                self.list_of_list.appendleft(i)
            return self.__next__()
        else:
            return self.list_of_list.popleft()
        
          
        
        
 
        
    
def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    # for i in FlatIterator(list_of_lists_2):
    #     print(i, end=', ')
    print(list(FlatIterator(list_of_lists_2)))
    # test_3()