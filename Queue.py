#!/usr/bin/env/ Python 3

# Name: John Asare
# Date: Fri Apr 27 19:06

""" Queue implemntation """


class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        return self.queue.pop()

    def peek(self):
        return self.queue[-1]

    def isEmpty(self):
        return self.queue == 0

    def size(self):
        return len(self.queue)


if __name__ == "__main__":
    line = Queue()
    line.enqueue("John")
    line.enqueue("Tom")
    line.enqueue("Sam")
    print('\n', "People standing on the line are: ", line.queue)

    line.enqueue("Mariam")
    line.enqueue("Liam")
    print('\n', "the line has expanded, these are the people now: ", line.queue)
    line.dequeue()
    line.dequeue()
    print('\n', "now there are these people on line? ", line.queue ,'\n')
    print("Is anyone on the line",line.isEmpty(), '\n',"How many people are on the line",
          line.size(), '\n',"Who is the last person on the line? ", line.peek())
