import time
import random
from collections import deque

class ArrayStack:
    def __init__(self):
        self.items = []
        self.author = "Сулыз Константин Викторович, 090304-РПИб-024"
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1] if self.items else None
    
    def contains(self, item):
        return item in self.items
    
    def is_empty(self):
        return len(self.items) == 0

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
        if self.head is None:
            return None
        popped = self.head.data
        self.head = self.head.next
        return popped
    
    def peek(self):
        return self.head.data if self.head else None
    
    def contains(self, item):
        current = self.head
        while current:
            if current.data == item:
                return True
            current = current.next
        return False
    
    def is_empty(self):
        return self.head is None

class LibraryStack:
    def __init__(self):
        self.items = deque()
        self.author = "Сулыз Константин Викторович, 090304-РПИб-024"
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1] if self.items else None
    
    def contains(self, item):
        return item in self.items
    
    def is_empty(self):
        return len(self.items) == 0

def check_king_moves(moves, stack_type):
    if stack_type == "array":
        stack = ArrayStack()
    elif stack_type == "linked_list":
        stack = LinkedListStack()
    else:  # "library"
        stack = LibraryStack()
    
    x, y = 0, 0
    stack.push((x, y))
    
    directions = {
        'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0),
        'UL': (-1, 1), 'UR': (1, 1), 'DL': (-1, -1), 'DR': (1, -1)
    }
    
    for move in moves:
        dx, dy = directions[move]
        x += dx
        y += dy
        if stack.contains((x, y)):
            return True
        stack.push((x, y))
    
    return False

def generate_moves(n):
    directions = ['U', 'D', 'L', 'R', 'UL', 'UR', 'DL', 'DR']
    return [random.choice(directions) for _ in range(n)]

def test_performance():
    move_counts = [100, 1000, 10000, 100000]
    implementations = [
        ("Array Stack", lambda m: check_king_moves(m, "array")),
        ("Linked List Stack", lambda m: check_king_moves(m, "linked_list")),
        ("Deque Stack", lambda m: check_king_moves(m, "library"))
    ]
    
    print("="*60)
    print("АВТОР: Сулыз Константин Викторович, группа 090304-РПИб-024")
    print("ПРОГРАММА: Определение повторных посещений шахматным королём")
    print("="*60)
    print("\nТЕСТИРОВАНИЕ ПРОИЗВОДИТЕЛЬНОСТИ РАЗЛИЧНЫХ РЕАЛИЗАЦИЙ СТЕКА\n")
    
    for n in move_counts:
        moves = generate_moves(n)
        print(f"Количество ходов: {n}")
        
        results = []
        for name, func in implementations:
            start_time = time.perf_counter()
            result = func(moves)
            elapsed = time.perf_counter() - start_time
            results.append((name, elapsed, result))
        
        # Сортируем по времени выполнения
        results.sort(key=lambda x: x[1])
        
        for name, elapsed, result in results:
            print(f"{name + ':':<20} {elapsed:.6f} сек | Результат: {'Есть повтор' if result else 'Нет повтора'}")
        
        print("\n" + "-"*50 + "\n")

def interactive_test():
    print("\nИНТЕРАКТИВНЫЙ РЕЖИМ ТЕСТИРОВАНИЯ")
    print("Введите последовательность ходов короля (U, D, L, R, UL, UR, DL, DR)")
    print("Разделяйте ходы пробелами. Пример: U D L R UL DR")
    print("Введите 'exit' для выхода\n")
    
    while True:
        user_input = input("Введите ходы: ").strip().upper()
        if user_input == 'EXIT':
            break
        
        moves = user_input.split()
        valid_moves = {'U', 'D', 'L', 'R', 'UL', 'UR', 'DL', 'DR'}
        
        if not all(move in valid_moves for move in moves):
            print("Ошибка: Некорректные ходы. Используйте только U, D, L, R, UL, UR, DL, DR")
            continue
        
        print("\nРезультаты для разных реализаций:")
        implementations = [
            ("Array Stack", "array"),
            ("Linked List Stack", "linked_list"),
            ("Deque Stack", "library")
        ]
        
        for name, stack_type in implementations:
            start_time = time.perf_counter()
            result = check_king_moves(moves, stack_type)
            elapsed = time.perf_counter() - start_time
            print(f"{name + ':':<20} {'Есть повтор' if result else 'Нет повтора'} | Время: {elapsed:.6f} сек")
        
        print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    test_performance()
    interactive_test()
