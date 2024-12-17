class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.table = [[] for _ in range(self.size)]

    def hash(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        index = self.hash(key)  
        if key not in self.table[index]:
            self.table[index].append(key)

    def remove(self, key: int) -> None:
        index = self.hash(key)  
        if key in self.table[index]:
            self.table[index].remove(key)

    def contains(self, key: int) -> bool:
        index = self.hash(key)  
        return key in self.table[index]
