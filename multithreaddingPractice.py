import time
import threading
import math

def caclSquares(arr):
    print("calculating squares")
    for i in arr:
        time.sleep(1)
        print('square', pow(i,2))


def calcCubes(arr):
    print("calculating cubes")
    for n in arr:
        time.sleep(1)
        print('cube',pow(n,3))

if __name__ == '__main__':
    arr = [1,2,4,4,5]
    t1 = threading.Thread(target=caclSquares,args=(arr,))
    t2 = threading.Thread(target=calcCubes,args=(arr,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("done printing")
