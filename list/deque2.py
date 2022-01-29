from collections import deque
import os
def search(lines, pattern, history=5):
    prevlines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, prevlines
        prevlines.append(line)
    




file_path = os.getcwd() + '/list/deque2.txt'
if __name__ == '__main__':
    with open(file_path) as f:
        for line, previous in search(f, 'python', 5):
            for prev in previous:
                print(prev, end='')
            print(line, end='')
            print('-'*20)
        # for line, previous in search(f, )