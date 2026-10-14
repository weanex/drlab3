
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    def __str__(self):
        return str(self.data)


class UnorderedList:
    def __init__(self):
        self.head = None


    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    #  №1.1 доработки
    def append(self, item):
        temp = Node(item)
        if self.head is None:
            self.head = temp
            return
        current = self.head
        while current.getNext() is not None:
            current = current.getNext()
        current.setNext(temp)

    def index(self, item):
        current = self.head
        pos = 0
        while current is not None:
            if current.getData() == item:
                return pos
            current = current.getNext()
            pos += 1
        raise ValueError(f"{item!r} is not in list")

    def insert(self, pos, item):
        if pos < 0:
            raise IndexError("negative index")
        if pos == 0:
            self.add(item)
            return
        if pos > self.size():
            raise IndexError("index out of range")
        temp = Node(item)
        current = self.head
        previous = None
        count = 0
        while count < pos:
            previous = current
            current = current.getNext()
            count += 1
        previous.setNext(temp)
        temp.setNext(current)

    def pop(self, pos=None):
        if self.head is None:
            raise IndexError("pop from empty list")

        if pos is None:
            current = self.head
            previous = None
            while current.getNext() is not None:
                previous = current
                current = current.getNext()
            if previous is None:
                self.head = None
            else:
                previous.setNext(None)
            return current.getData()

        if pos < 0 or pos >= self.size():
            raise IndexError("pop index out of range")

        if pos == 0:
            data = self.head.getData()
            self.head = self.head.getNext()
            return data

        current = self.head
        previous = None
        count = 0
        while count < pos:
            previous = current
            current = current.getNext()
            count += 1
        previous.setNext(current.getNext())
        return current.getData()

    #  №1.2 __str__ 
    def __str__(self):
        items = []
        current = self.head
        while current is not None:
            items.append(str(current.getData()))
            current = current.getNext()
        return "[" + ", ".join(items) + "]"

    #  №1.3 срез 
    def slice(self, start, stop):
        """Вернуть новый UnorderedList с элементами [start, stop)."""
        if start < 0 or stop < 0:
            raise IndexError("negative index")
        if start > stop:
            raise IndexError("start > stop")
        result = UnorderedList()
        current = self.head
        pos = 0
        collected = []
        while current is not None and pos < stop:
            if pos >= start:
                collected.append(current.getData())
            current = current.getNext()
            pos += 1
        for x in collected:
            result.append(x)
        return result


#  ТЕСТЫ 
if __name__ == "__main__":
    print("Задание №1 ")

    lst = UnorderedList()
    assert lst.is_empty() is True

    # add
    for x in [3, 2, 1]:
        lst.add(x)
    assert str(lst) == "[1, 2, 3]", str(lst)
    print("add + __str__:", lst)

    # append
    lst.append(4)
    lst.append(5)
    assert str(lst) == "[1, 2, 3, 4, 5]", str(lst)
    print("append:", lst)

    # size
    assert lst.size() == 5
    print("size:", lst.size())

    # search
    assert lst.search(3) is True
    assert lst.search(99) is False
    print("search 3:", lst.search(3), "| search 99:", lst.search(99))

    # index
    assert lst.index(1) == 0
    assert lst.index(5) == 4
    print("index(1) =", lst.index(1), "| index(5) =", lst.index(5))

    try:
        lst.index(100)
        assert False, "должно быть ValueError"
    except ValueError:
        print("index(100) -> ValueError OK")

    # insert
    lst.insert(0, 0)
    assert str(lst) == "[0, 1, 2, 3, 4, 5]", str(lst)
    lst.insert(3, 99)
    assert str(lst) == "[0, 1, 2, 99, 3, 4, 5]", str(lst)
    print("insert:", lst)

    # pop (последний)
    v = lst.pop()
    assert v == 5
    assert str(lst) == "[0, 1, 2, 99, 3, 4]", str(lst)
    print("pop():", v, "->", lst)

    # pop(pos)
    v = lst.pop(2)
    assert v == 2
    assert str(lst) == "[0, 1, 99, 3, 4]", str(lst)
    print("pop(2):", v, "->", lst)

    v = lst.pop(0)
    assert v == 0
    assert str(lst) == "[1, 99, 3, 4]", str(lst)
    print("pop(0):", v, "->", lst)

    # remove
    lst.remove(99)
    assert str(lst) == "[1, 3, 4]", str(lst)
    print("remove(99):", lst)

    # slice
    lst2 = UnorderedList()
    for x in range(10):
        lst2.append(x)   # [0..9]
    s = lst2.slice(2, 6)
    assert str(s) == "[2, 3, 4, 5]", str(s)
    print("slice(2,6) из", lst2, "->", s)

    s2 = lst2.slice(0, 0)
    assert str(s2) == "[]"
    print("slice(0,0) ->", s2)

    s3 = lst2.slice(5, 100)   # stop больше размера — берём до конца
    assert str(s3) == "[5, 6, 7, 8, 9]", str(s3)
    print("slice(5,100) ->", s3)

