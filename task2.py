
from task1_unordered_list import UnorderedList, Node


def move_to_front(strings):
    lst = UnorderedList()
    for s in strings:
        if lst.search(s):
            lst.remove(s)
        lst.add(s)
    return lst


#  ТЕСТЫ 
if __name__ == "__main__":
    print("Задание №2:")


    data = ["a", "b", "c", "a", "b"]
    lst = move_to_front(data)
    print("Ввод:", data)
    print("Результат:", lst)
    assert str(lst) == "[b, a, c]", str(lst)

   
    data2 = ["x", "y", "z", "x", "x"]
    lst2 = move_to_front(data2)
    print("Ввод:", data2)
    print("Результат:", lst2)
    assert str(lst2) == "[x, z, y]", str(lst2)


    print("\nВведите строки через пробел для проверки (Enter — пропустить):")
    line = input().strip()
    if line:
        user = line.split()
        print("Результат:", move_to_front(user))

