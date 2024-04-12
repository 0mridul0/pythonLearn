import pandas as pd
class hashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
    def get_hash(self,key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    def __getitem__(self,index):
        h = self.get_hash(index)
        for element in self.arr[h]:
            if element[0]==index:
                return element[1]
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        found = False
        for idx,element in enumerate(self.arr[h]):
            if(len(element)==2 and element[0]==key):
                self.arr[h][idx] = (key,val)
                found = True
                break
        if not found:
            self.arr[h].append((key,val))
    def __delitem__(self,key):
        h = self.get_hash(key)
        for index,kn in enumerate(self.arr[h]):
            if kn[0] == key:
                del self.arr[h][index]


    

if __name__ == '__main__':
     df = pd.read_csv('nyc_weather.csv')
     
    #  arr = df.to_dict(orient='records')
    #  arr2 = dict(arr)
     print(df)
     h1 = hashTable()
     h1['march 1'] = 130
     h1['march 2'] = 120
     h1['march 6'] = 200
     h1['march 17'] = 234
    #  print(h1.arr)
    #  abc = h1.get_hash('march 6')
    #  bcd = h1.get_hash('march 17')
    #  print(str(abc) + " " + str(bcd))
    #  print(h1['march 17'])
    #  del h1['march 17']
    #  print(h1.arr)
