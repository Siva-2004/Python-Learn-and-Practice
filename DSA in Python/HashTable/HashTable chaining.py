class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for i, ele in enumerate(self.arr[h]):
            if ele[0] == key and len(ele) == 2:
                self.arr[h][i] = (key, value)
                found = True
        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for ele in self.arr[h]:
            if ele[0] == key:
                return ele[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for i, ele in enumerate(self.arr[h]):
            if ele[0] == key:
                del self.arr[h][i]


if __name__ == "__main__":
    ht = HashTable()
    ht["August 19"] = "Monday"
    ht["August 19"] = "Holiday"
    ht["August 20"] = "Tuesday"
    ht["August 28"] = "Wednesday"
    print(ht.arr)
    print(ht["August 28"])
    del ht["August 28"]
    print(ht.arr)
