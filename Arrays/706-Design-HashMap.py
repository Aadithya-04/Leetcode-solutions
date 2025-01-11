class MyHashMap:

    def __init__(self):
        # Initialize the hash map with a list of None values.
        self.size = 1000  # Size of the hash map
        self.map = [[] for _ in range(self.size)]  # List of lists to handle collisions

    def _hash(self, key: int) -> int:
        # Hash function that maps the key to an index in the array
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        # Check if the key already exists in the list at this index
        for i, (k, v) in enumerate(self.map[index]):
            if k == key:
                # If the key exists, update the value
                self.map[index][i] = (key, value)
                return
        # Otherwise, add a new key-value pair
        self.map[index].append((key, value))

    def get(self, key: int) -> int:
        index = self._hash(key)
        # Search for the key in the list at the hashed index
        for k, v in self.map[index]:
            if k == key:
                return v
        # If not found, return -1
        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)
        # Search for the key in the list at the hashed index
        for i, (k, v) in enumerate(self.map[index]):
            if k == key:
                # Remove the key-value pair if found
                del self.map[index][i]
                return
