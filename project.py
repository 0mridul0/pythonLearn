if __name__ == '__main__':
    n = int(input())
    arr = input().split()
    set1 = set()
    for i in arr:
        set1.add(i)
    print(set1)
    arr2 = list(set1)
    print(arr2)
    arr2.sort()
    print(arr2)
    print(arr2[-2])
    
    