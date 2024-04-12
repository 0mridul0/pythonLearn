class hashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
    def get_hash(self,key):
        hash = 0
        for char in key:
            hash =+ ord(char)
        return hash % self.MAX
    def __getitem__(self,index):
        h = self.get_hash(index)
        return self.arr[h]
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        self.arr[h] = val

if __name__ == '__main__':
     h1 = hashTable()
     h1['march 1'] = 130
     h1['march 2'] = 120
     h1['march 6'] = 200
     print(h1.arr)
     print(h1['march 6'])