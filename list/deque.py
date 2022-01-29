from collections import deque
import os
file_path = os.getcwd() + "\list\deque.txt"
def tail(file_path, n= 4):
    with open(file_path, 'r') as f:
        return deque(f, n)

# print(tail(file_path))

def roundrobin(*iterables):
    iterables = deque(map(iter, iterables))
    while iterables:
        try:
            yield next(iterables[0])
            iterables.rotate(-1)
        except StopIteration:
            iterables.popleft()

# for i in roundrobin('ABC', 'D', 'EF'):
#     print(i)