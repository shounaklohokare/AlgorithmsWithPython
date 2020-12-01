class HashTable:

    def __init__(self, size):
        self.size = 0
        self.slots = [None] * self.size
        self.data = [None] * self.size


    def put(self, key, data):

        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue]==None:
            self.slots[hashvalue]=key
            self.data[hashvalue]=data

        else:

            if self.slots[hashvalue]==key:
                self.data[hashvalue]=data

            else:

                rehashvalue = self.rehash(hashvalue, len(self.slots))

                while self.slots[rehashvalue]!=None and self.slots[rehashvalue]!=key:
                    self.rehash(rehashvalue, len(self.slots))

                self.slots[rehashvalue]=key
                self.data[rehashvalue] = data


    def hashfunction(self, key, size):
        return key % self.size

    def rehash(self, oldhash, key, size):
        return (oldhash+1)%size


    def get(self, key):

        startslot = self.hashfunction(key, len(self.size))

        found = False
        stop = False

        data = None

        position = startslot

        while self.slots[position]!=None and not stop and not found:

            if self.slots[position]==key:
                found=True
                data = self.data[position]

            else:
                position = self.rehash(position, len(self.slots))

                if position==startslot:
                    stop = False

        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.put(key, value)