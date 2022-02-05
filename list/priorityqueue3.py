class PriorityQueue():
    def __init__(self):
        self._queue = []

    def insert(self, value):
        self._queue.append(value)

    def isEmpty(self):
        return len(self._queue) == 0

    def size(self):
        return len(self._queue)

    def delete(self):
        max = 0
        for i in range(len(self._queue)):
            if self._queue[i] > self._queue[max]:
                max = i
        item = self._queue[max]
        del self._queue[max]
        return item

if __name__ == '__main__':
    myQueue = PriorityQueue()
    myQueue.insert(12)
    myQueue.insert(1)
    myQueue.insert(14)
    myQueue.insert(7)
    print(myQueue)            
    while not myQueue.isEmpty():
        print(myQueue.delete()) 