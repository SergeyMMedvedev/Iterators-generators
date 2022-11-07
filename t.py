list_of_lists_2 = [
    [['a'], ['b', 'c']],
    ['d', 'e', [['f'], 'h'], False],
    [1, 2, None, [[[[['!']]]]], []]
]
res = []
def f(l, el):

    if not l:
        return 
    el = l[0]

    if not isinstance(el, list):
        res.append(el)
    else:
        l.pop(0)
        f(el)

print(f(list_of_lists_2))

print(res)