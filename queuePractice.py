from collections import deque
class Queue:
    def __init__(self) -> None:
        self.buffer = deque()
    def enqueue(self,val):
        self.buffer.appendleft(val)
    def dequeue(self):
        self.buffer.pop()
    def isEmplty(self):
        return len(self.buffer)==0
    def size(self):
        return len(self.buffer)
if __name__ == '__main__':
    qu = Queue()
    


