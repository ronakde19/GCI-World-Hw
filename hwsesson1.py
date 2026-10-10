import numpy as np

arr = np.array([1, 5, 10, 3, 4, 25, 30, 35])


def homework(a):
    result = a[(a%5==0) & (a%2==1)]
    return result

answer = home work(arr)

print(answer)