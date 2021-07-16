class HashTable:
    """
    Basic Hash Table
    """

    def __init__(self, size_table: int):
        self.size_table = size_table
        self.table = [[] for i in range(self.size_table)]
        self._keys = {}

    def keys(self):
        return self._keys

    def __hash_function(self, key: str) -> int:
        hashed_value = hash(key)
        return hashed_value % self.size_table

    def insert(self, key: str, value: str) -> None:
        index = self.__hash_function(key)
        self.table.insert(index, (key, value))

    def get_value(self, key: str):
        index = self.__hash_function(key)
        return self.table[index]


if __name__ == "__main__":
    table = HashTable(20)
    print(hash("test"))
    print(hash("test") % 20)

    print(table.table)
    table.insert("test", 99)
    print(table.table)
    print(table.get_value("test"))
