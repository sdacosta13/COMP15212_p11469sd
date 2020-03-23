import queue
import hashlib
from random import randrange


# Various implementations of caching.
class Memory:
    def __init__(self):
        self.hit_count = 0

    def get_hit_count(self):
        return self.hit_count

    def name(self):
        return "Memory"

    def lookup(self, address):
        # This one actually has no cache, so every lookup
        # requires a memory hit.
        print("Memory Access", end=" ")
        self.hit_count += 1
        string = str(address ^ 3).encode()
        return hashlib.md5(string).hexdigest()[:8]


class CyclicCache(Memory):
    def name(self):
        return "Cyclic"

    # Edit the code below to provide an implementation of a cache that
    # uses a cyclic caching strategy with a cache size of 4. You can
    # use additional methods and variables as you see fit as long as you
    # provide a suitable overridding of the lookup method.

    def __init__(self):
        super().__init__()
        self.cache = []
        self.pointer = 0
        self.size = 4
        for i in range(self.size):
            self.cache.append(None)
        print(self.cache)
    def lookup(self, address):
        string = str(address ^ 3).encode()
        string = hashlib.md5(string).hexdigest()[:8]
        inCache = False
        for i in range(self.size):
            if(string == self.cache[i]):
                inCache = True
                break
        if(inCache):
            print("Cache hit", end=" ")
        else:
            print("Memory Access", end=" ")
            self.hit_count += 1
            if(self.pointer < self.size):
                self.cache[self.pointer] = string
                self.pointer += 1
            else:
                self.cache[0] = string
                self.pointer = 1



        return string



class LRUCache(Memory):
    def name(self):
        return "LRU"

    # Edit the code below to provide an implementation of a cache that
    # uses a least recently used caching strategy with a cache size of
    # 4. You can use additional methods and variables as you see fit as
    # long as you provide a suitable overridding of the lookup method.

    def __init__(self):
        super().__init__()
        self.cache = [
            [None, 0],
            [None, 0],
            [None, 0],
            [None, 0]
        ]
        self.size = 4

    def lookup(self, address):
        inCache = False
        string = str(address ^ 3).encode()
        string = hashlib.md5(string).hexdigest()[:8]
        for i in range(self.size):
            if(string == self.cache[i][0]):
                inCache = True
                self.cache[i][1] += 1
                break
        if(inCache):
            print("Cache hit", end = " ")
        else:
            print("Memory Access", end = " ")
            self.hit_count += 1
            minUse = self.cache[0][1]
            minUseLoc = 0

            for itemLoc in range(self.size):
                item = self.cache[itemLoc]
                if(item[1] < minUse):
                    minUse = item[1]
                    minUseLoc = itemLoc
            self.cache[minUseLoc] = [string,0]
        return string
