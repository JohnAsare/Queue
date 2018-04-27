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
        return self.queue == []

    def size(self):
        return len(self.queue)