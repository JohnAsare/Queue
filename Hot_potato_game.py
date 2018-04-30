#!/usr/bin/env/ Python 2

# Name: John Asare
# Date: Mon Apr 30 16:56


""" Queue implementation to make a game based on the story "Josehphus" problem
visit: https://en.wikipedia.org/wiki/Josephus_problem for details on the story"""


class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)

    def peek(self):
        return self.queue[-1]

