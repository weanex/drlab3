# task5_double_list.py


class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.data)


class DoubleList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def is_empty(self):
        return self.head is None

    def size(self):
        return self._size

    def search(self, item):
        cur = self.head
        while cur is not None:
            if cur.data == item:
                return True
            cur = cur.next
        return False

    def add_front(self, item):
        n = DNode(item)
        if self.head is None:
            self.head = self.tail = n
        else:
            n.next = self.head
            self.head.prev = n
            self.head = n
        self._size += 1

    def add_rear(self, item):
        n = DNode(item)
        if self.tail is None:
            self.head = self.tail = n
        else:
            n.prev = self.tail
            self.tail.next = n
            self.tail = n
        self._size += 1

    def remove_front(self):
        if self.head is None:
            raise IndexError("remove from empty list")
        data = self.head.data
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        self._size -= 1
        return data

    def remove_rear(self):
        if self.tail is None:
            raise IndexError("remove from empty list")
        data = self.tail.data
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        self._size -= 1
        return data

    def _find_node(self, item):
        cur = self.head
        while cur is not None:
            if cur.data == item:
                return cur
            cur = cur.next
        return None

    def insert_before(self, node, item):
        if node is None or node is self.head:
            self.add_front(item)
            return
        n = DNode(item)
        n.prev = node.prev
        n.next = node
        node.prev.next = n
        node.prev = n
        self._size += 1

    def insert_after(self, node, item):
        if node is None or node is self.tail:
            self.add_rear(item)
            return
        n = DNode(item)
        n.next = node.next
        n.prev = node
        node.next.prev = n
        node.next = n
        self._size += 1

    def remove_node(self, node):
        if node is None:
            raise ValueError("node is None")
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next is not None:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        self._size -= 1

    def __str__(self):
        items = []
        cur = self.head
        while cur is not None:
            items.append(str(cur.data))
            cur = cur.next
        return "[" + ", ".join(items) + "]"

    def reverse_str(self):
        items = []
        cur = self.tail
        while cur is not None:
            items.append(str(cur.data))
            cur = cur.prev
        return "[" + ", ".join(items) + "]"


if __name__ == "__main__":
    print(" Задание №5:")

    dl = DoubleList()
    assert dl.is_empty() is True
    assert dl.size() == 0

    dl.add_front(2)
    dl.add_front(1)
    dl.add_rear(3)
    dl.add_rear(4)
    assert str(dl) == "[1, 2, 3, 4]", str(dl)
    assert dl.reverse_str() == "[4, 3, 2, 1]", dl.reverse_str()
    assert dl.size() == 4
    print("add_front/add_rear:", dl, "| reverse:", dl.reverse_str())

    assert dl.search(3) is True
    assert dl.search(99) is False
    print("search(3):", dl.search(3), "| search(99):", dl.search(99))

    assert dl.remove_front() == 1
    assert dl.remove_rear() == 4
    assert str(dl) == "[2, 3]", str(dl)
    print("remove_front/remove_rear:", dl)

    node2 = dl._find_node(2)
    node3 = dl._find_node(3)
    dl.insert_before(node3, 99)
    dl.insert_after(node2, 88)
    assert str(dl) == "[2, 88, 99, 3]", str(dl)
    print("insert_before/after:", dl)

    dl.remove_node(dl._find_node(88))
    assert str(dl) == "[2, 99, 3]", str(dl)
    print("remove_node(88):", dl)

    dl.remove_node(dl._find_node(2))
    dl.remove_node(dl._find_node(3))
    assert str(dl) == "[99]", str(dl)
    print("remove head & tail:", dl)

    dl.remove_node(dl._find_node(99))
    assert dl.is_empty() and dl.size() == 0
    print("empty:", dl, "size =", dl.size())