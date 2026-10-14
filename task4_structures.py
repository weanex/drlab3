# task4_structures.py

import time
from collections import deque
from task1_unordered_list import UnorderedList


class Stack:
    def __init__(self):
        self._lst = UnorderedList()

    def is_empty(self):
        return self._lst.is_empty()

    def push(self, item):
        self._lst.add(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._lst.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._lst.head.getData()

    def size(self):
        return self._lst.size()

    def __str__(self):
        return "Stack(" + str(self._lst) + ")"


class Queue:
    def __init__(self):
        self._lst = UnorderedList()

    def is_empty(self):
        return self._lst.is_empty()

    def enqueue(self, item):
        self._lst.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._lst.pop(0)

    def size(self):
        return self._lst.size()

    def __str__(self):
        return "Queue(" + str(self._lst) + ")"


class Deque:
    def __init__(self):
        self._lst = UnorderedList()

    def is_empty(self):
        return self._lst.is_empty()

    def size(self):
        return self._lst.size()

    def add_front(self, item):
        self._lst.add(item)

    def add_rear(self, item):
        self._lst.append(item)

    def remove_front(self):
        if self.is_empty():
            raise IndexError("remove_front from empty deque")
        return self._lst.pop(0)

    def remove_rear(self):
        if self.is_empty():
            raise IndexError("remove_rear from empty deque")
        return self._lst.pop()

    def __str__(self):
        return "Deque(" + str(self._lst) + ")"


def test_stack():
    s = Stack()
    assert s.is_empty()
    for x in [1, 2, 3]:
        s.push(x)
    assert s.size() == 3
    assert s.peek() == 3
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.is_empty()
    print("Stack OK")


def test_queue():
    q = Queue()
    assert q.is_empty()
    for x in [1, 2, 3]:
        q.enqueue(x)
    assert q.size() == 3
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.is_empty()
    print("Queue OK")


def test_deque():
    d = Deque()
    assert d.is_empty()
    d.add_front(2)
    d.add_front(1)
    d.add_rear(3)
    d.add_rear(4)
    assert str(d) == "Deque([1, 2, 3, 4])", str(d)
    assert d.remove_front() == 1
    assert d.remove_rear() == 4
    assert d.remove_front() == 2
    assert d.remove_rear() == 3
    assert d.is_empty()
    print("Deque OK")


def benchmark():
    N = 5000

    print(f"\n Эксперимент: N = {N}\n")

    t0 = time.perf_counter()
    s = []
    for i in range(N):
        s.append(i)
    while s:
        s.pop()
    t_py_stack = time.perf_counter() - t0

    t0 = time.perf_counter()
    s = Stack()
    for i in range(N):
        s.push(i)
    while not s.is_empty():
        s.pop()
    t_ll_stack = time.perf_counter() - t0

    print(f"Стек: Python list = {t_py_stack:.4f}s | UnorderedList = {t_ll_stack:.4f}s")

    t0 = time.perf_counter()
    q = deque()
    for i in range(N):
        q.append(i)
    while q:
        q.popleft()
    t_py_queue = time.perf_counter() - t0

    t0 = time.perf_counter()
    q = Queue()
    for i in range(N):
        q.enqueue(i)
    while not q.is_empty():
        q.dequeue()
    t_ll_queue = time.perf_counter() - t0

    print(f"Очередь: collections.deque = {t_py_queue:.4f}s | UnorderedList = {t_ll_queue:.4f}s")

    t0 = time.perf_counter()
    d = deque()
    for i in range(N):
        d.append(i)
    while d:
        d.popleft()
    t_py_deque = time.perf_counter() - t0

    t0 = time.perf_counter()
    d = Deque()
    for i in range(N):
        d.add_rear(i)
    while not d.is_empty():
        d.remove_front()
    t_ll_deque = time.perf_counter() - t0

    print(f"Дек:   collections.deque = {t_py_deque:.4f}s | UnorderedList = {t_ll_deque:.4f}s")


if __name__ == "__main__":
    print(" Задание №4:")
    test_stack()
    test_queue()
    test_deque()
    benchmark()