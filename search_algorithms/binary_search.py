import random
lst = [1,2,3,4,5,6,7,8,9,10,11,15,3000]
#for i in range(10):
    #lst.append(random.randint(0,100))
#lst.sort()

def binary_search(lst,n):
    bot = 0
    top = len(lst)
    while True:
        index = (top-bot)//2
        if top-1 == bot:
            return False
        elif lst[index] == n:
            return True
        elif lst[index] > n:
            top = index
        elif lst[index] < n:
            bot = index

def rec_search(lst,n):
    bot = 0
    top = len(lst)
    index = (top-bot)//2
    if lst[0] == n:
        return True
    elif top <= 2:
        return False
    elif lst[index] >= n:
        return rec_search(lst[bot:index],n)
    elif lst[index] <= n:
        return rec_search(lst[index:top],n)

def binary(a):
    b = ''
    while (a > 0):
        remainder = a%2
        a = a//2
        b += str(remainder)
    return b[::-1]
