class HashMap:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        if self.arr[h] is None or self.arr[h] == value:
            self.arr[h] = (key, value)
        else:
            i = 1
            done = False
            while not done:
                index = (h + i) % self.MAX
                if index == h:
                    print("HashMap is full")
                    break
                if self.arr[index] is None or self.arr[h] == value:
                    self.arr[index] = (key, value)
                    done = True
                else:
                    i += 1

    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h][0] == key:
            return self.arr[h][1]
        i = 1
        done = False
        while not done:
            index = (h + i) % self.MAX
            if index == h:
                return "Invalid index."
                done = True
            if self.arr[index][0] == key:
                return self.arr[index][1]
            i += 1

    def __delitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h][0] == key:
            self.arr[h] = None
            return
        i = 1
        done = False
        while not done:
            index = (h + i) % self.MAX
            if index == h:
                return "Invalid index."
                done = True
            if self.arr[index][0] == key:
                self.arr[index] = None
            i += 1


if __name__ == "__main__":
    hm = HashMap()
    print(hm.arr)
    hm["1"] = "Chelsea"
    hm["2"] = "Manchester City"
    hm["3"] = "Liverpool"
    hm["4"] = "Arsenal"
    hm["5"] = "Manchester United"
    hm["6"] = "Tottenham Hotspur"
    hm["7"] = "Aston villa"
    hm["8"] = "Newcastle United"
    hm["9"] = "Ipswich Town"
    hm["0"] = "Everton FC"
    print(hm.arr)
    hm["11"] = "Wolverhampton Wanderers"
    print(hm["11"])
    print(hm["3"])
    del hm["0"]
    print(hm.arr)
    hm["11"] = "Wolverhampton Wanderers"
    print(hm.arr)
