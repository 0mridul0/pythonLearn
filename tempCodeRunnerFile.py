# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
set1 = set(input().split())
N = int(input())
for i in range(N):
    str = (input().split())
    if(str[0] == 'remove'):
        set1.remove(str[1])
    elif(str[0]=='discard'):
        set1.discard(str[1])
    elif(str[0]=='pop'):
        set1.pop()
li1 = list(set1)
sum = 0
for i in li1:
    sum += int(i)
print(sum)
    