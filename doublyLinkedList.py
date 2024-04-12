class Node:
    def __init__(self,data = None,next = None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev
class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    #insert at head
    def insertAtHead(self,data):
        node = Node(data,self.head)
        if self.tail is None:
            self.tail=node
        self.head = node
    #insert at end
    def insertAtEnd(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)
        itr.next.prev = itr
        self.tail = Node
    #insert data at particular index
    def insertAtIndex(self,data,index):
        if index<0 or index>self.lenList():
            raise Exception("invalid index")
        if index==0:
            self.insertAtHead(self,data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data,itr.next,itr)
                itr.next = node
                break
            itr = itr.next
            count +=1

    #print list
    def printList(self):
        if self.head is None:
            print("list empty")
        else:
            listPr = ""
            itr = self.head
            while itr:
                listPr += str(itr.data) + "-->"
                itr = itr.next
            print(listPr)
    #reverse print a list
    def reversePrint(self):
        itr = self.tail
        ptintLr = ""
        while itr:
            if self.tail is None:
                print("emplty list")
            else:
                ptintLr += str(itr.data) + "-->"
                itr = itr.prev
        print(ptintLr)
    #insert via llist
    def insertValues(self,data):
            self.head = None
            for i in data:
                self.insertAtEnd(i)
    #length of linked list
    def lenList(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next
        return count
    #remove element at a particular index
    def removeAtIndex(self,index):
        if index<0 or index>=self.lenList():
            raise Exception("invalid intex")
        if index == 0:
            self.head.next.prev = None
            self.head = self.head.next
            return
        else:
            count = 0 
            itr = self.head
            while itr:
                if count == index-1:
                    itr.next = itr.next.next
                    break
                itr = itr.next
                count += 1
    
            

if __name__ == '__main__':
    ll = linkedList()
    # ll.insertAtHead(5)
    # ll.insertAtHead(10)  
    # ll.insertAtEnd(15)
    # ll.insertAtEnd(20)
    # ll.printList()
    # print(ll.lenList())
    ll.insertValues([3,4,6,7,10,12])
    # ll.printList()
    # ll.removeAtIndex(1)
    ll.printList()
    # print(ll.lenList())
    # ll.insertAtIndex(8,4)
    ll.printList()
    ll.reversePrint()

            

    