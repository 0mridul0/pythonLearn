from collections import deque
class Stack:
     def __init__(self):
        self.container = deque()
     def push(self,val):
        self.container.append(val)
     def pop(self):
        self.container.pop()
     def peek(self):
        return self.container[-1]
     def isEmpty(self):
        return len(self.container)==0
     def size(self):
        return len(self.container)
def balanceParanthesis(str):
    st = Stack()
    for i in str:
        if (i=='[' or i=='{' or i=='('):
             st.push(i)
        elif(i==']' and st.peek()=='['):
            st.pop()
        elif(i=='}' and st.peek()=='{'):
            st.pop()
        elif(i==')' and st.peek()=='('):
            st.pop()
    if st.size() < 1:
        return True
    else:
        return False        

    
    
if __name__ == '__main__':
#    balanceParanthesis("mridul")
    print(balanceParanthesis('{{(([]))}}{[}[]()'))
      
