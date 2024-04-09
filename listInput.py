list = []
for i in range(3):
    list.append(int(input()))
print(list)
list2 = list.copy()
list2.reverse()
print(list2)
if(list == list2):
    print(True)