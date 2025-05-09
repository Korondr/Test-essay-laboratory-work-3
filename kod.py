import timeit
from collections import deque

# Реализация стека через массив
class ArrayStack:
    def __init__(self):
        self.items = []
        self.author = "Сулыз Константин Викторович, 090304-РПИб-024"

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Peek from empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

# Реализация стека через связанный список
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.head = None
        self.author = "Сулыз Константин Викторович, 090304-РПИб-024"

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if not self.is_empty():
            popped = self.head.data
            self.head = self.head.next
            return popped
        else:
            raise IndexError("Pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.head.data
        else:
            raise IndexError("Peek from empty stack")

    def is_empty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def __str__(self):
        items = []
        current = self.head
        while current:
            items.append(str(current.data))
            current = current.next
        return "[" + ", ".join(reversed(items)) + "]"

# Реализация стека с использованием deque
class LibraryStack:
    def __init__(self):
        self.items = deque()
        self.author = "Сулыз Константин Викторович, 090304-РПИб-024"

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Peek from empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(list(self.items))

# Функция для тестирования стека
def test_stack(stack_class, operations):
    stack = stack_class()
    for op in operations:
        if op[0] == 'push':
            stack.push(op[1])
        elif op[0] == 'pop':
            stack.pop()
    return stack

# Основная часть программы
if __name__ == "__main__":
    
    operations = [('push', i) for i in range(10000)] + [('pop', None) for _ in range(10000)]

    print("Автор: Сулыз Константин Викторович, 090304-РПИб-024")
    print("\nТестирование производительности реализаций стека...")

    # Тестируем каждую реализацию
    implementations = [
        ("Стек на массиве", ArrayStack),
        ("Стек на связанном списке", LinkedListStack),
        ("Стек из стандартной библиотеки (deque)", LibraryStack)
    ]

    for name, impl in implementations:
        time = timeit.timeit(lambda: test_stack(impl, operations), number=10)
        print(f"{name}: {time:.4f} секунд (10 итераций)")
