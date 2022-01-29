records = [
    ('foo', 1 , 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]


def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

items = [1, 10, 7, 4, 5, 9]
print(sum(items))