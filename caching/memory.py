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
        print("Memory Access", end = " ")
        self.hit_count += 1
        string = str(address ^ 3).encode()
        return hashlib.md5(string).hexdigest()[:8]


class CyclicCache(Memory):
    def name(self):
        return "Cyclic"

    # Edit the code below to provide an implementation of a cache that
    # uses a cyclic caching strategy with a cache size of 4. You can
    # use additional methods and variables as you see fit as long as you
    # provide a suitable overridding of the lookup methodself.


    def __init__(self):
        super().__init__()
        self.cache = []
        self.pointer = 0
        self.size = 4
        for i in range(self.size):
            self.cache.append([None, None])


    def lookup(self, address):
        inCache = False
        for i in range(self.size):
            if(address == self.cache[i][0]):
                inCache = True
                break
        if(inCache):
            val = self.cache[i][1]
        else:
            val = super().lookup(address)
            if(self.pointer < self.size):
                self.cache[self.pointer] = [address, val]
                self.pointer += 1
            else:
                self.cache[0] = [address,val]
                self.pointer = 1
        return val


class LRUCache(Memory):
    def name(self):
        return "LRU"

    # Edit the code below to provide an implementation of a cache that
    # uses a least recently used caching strategy with a cache size of
    # 4. You can use additional methods and variables as you see fit as
    # long as you provide a suitable overridding of the lookup method.


    def __init__(self):
        super().__init__()
        self.cache = []
        self.size = 4
        for i in range(self.size):
            self.cache.append(list([None, None, 0]))


    def lookup(self, address):
        inCache = False
        for i in range(self.size):
            if(address == self.cache[i][0]):
                inCache = True
                self.cache[i][2] += 1
                break
        if(inCache):
            val = self.cache[i][1]
            self.cache[i][2] = 0
            self.increaseTimeLived()


        else:
            val = super().lookup(address)
            maxVal = 0
            maxLoc = 0
            for i in range(self.size):
                if self.cache[i][2] > maxVal:
                    maxVal = self.cache[i][2]
                    maxLoc = i
            self.cache[maxLoc] = [address,val, 0]
            self.increaseTimeLived()


        return val

    def increaseTimeLived(self):
        for i in range(self.size):
            self.cache[i][2] += 1
