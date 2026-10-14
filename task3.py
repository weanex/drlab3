
from task1_unordered_list import Node


def reverse_iterative(head):
    prev = None
    current = head
    while current is not None:
        nxt = current.getNext()
        current.setNext(prev)
        prev = current
        current = nxt
    return prev


def reverse_recursive(head):
    if head is None or head.getNext() is None:
        return head
    new_head = reverse_recursive(head.getNext())
    head.getNext().setNext(head)
    head.setNext(None)
    return new_head


def build_list(values):
    head = None
    for v in reversed(values):
        n = Node(v)
        n.setNext(head)
        head = n
    return head


def to_python_list(head):
    res = []
    cur = head
    while cur is not None:
        res.append(cur.getData())
        cur = cur.getNext()
    return res


#  ТЕСТЫ 
if __name__ == "__main__":
    print(" Задание №3:")

    for values in ([1, 2, 3, 4, 5], [42], [], [1, 2]):
        h1 = build_list(values)
        h1 = reverse_iterative(h1)
        r1 = to_python_list(h1)
        print(f"iterative {values} -> {r1}")
        assert r1 == list(reversed(values))

        h2 = build_list(values)
        h2 = reverse_recursive(h2)
        r2 = to_python_list(h2)
        print(f"recursive {values} -> {r2}")
        assert r2 == list(reversed(values))
