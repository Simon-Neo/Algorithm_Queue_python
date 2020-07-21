class Queue:
    def __init__(self, mem_len):
        self.mem_len = mem_len
        self.queue = [0 for i in range(self.mem_len)]

        self.head = 0
        self.tail = 0

    def render(self):
        print(self.queue)
        print('head = ',self.head % self.mem_len)
        print('tail = ',self.tail % self.mem_len)

    def size(self):
        return self.tail - self.head

    def push(self, data):
        if self.size() >= self.mem_len:
            print('Queue is full. Sorry!')
            return

        self.queue[self.tail % self.mem_len] = data
        self.tail += 1
    def pop(self):
        if self.size() <= 0:
            return -1
        tail_data = self.queue[self.head % self.mem_len]
        self.queue[self.head % self.mem_len] = 0
        self.head += 1
        return tail_data

    def empty(self):
        if self.size() > 0:
            return 0
        else:
            return 1

    def front(self):
        if self.size() <= 0:
            return -1
        else:
            return self.queue[self.head % self.mem_len]
    def back(self):
        if self.size() <= 0:
            return -1
        else:
            return self.queue[(self.tail - 1) % self.mem_len]

import sys

# print('How many times order ? :')
# times = int(sys.stdin.readline())
queue = Queue(5)

times = 2000

for _ in range(times):
    inputs = sys.stdin.readline().split()
    #inputs = text.split()
    order = None
    data = None

    if len(inputs) != 1:
        data = int(inputs[1])
    order = inputs[0]

    if order.lower() == 'push':
        queue.push(data)
    elif order.lower() == 'pop':
        print(queue.pop())
    elif order.lower() == 'size':
        print(queue.size())
    elif order.lower() == 'empty':
        print(queue.empty())
    elif order.lower() == 'front':
        print(queue.front())
    elif order.lower() == 'back':
        print(queue.back())
    else:
        print("It's wrong command try again... -_-;;;")

    queue.render()







