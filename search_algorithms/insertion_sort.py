lst = [5,3,2,7,6,3,8,1,2,3,3444]

def insert_sort(lst):
    steps = 0
    for i in range(len(lst)):
        k = i 
        while k != 0 and lst[k] < lst[k-1]:
            x = lst[k]
            lst[k] = lst[k-1]
            lst[k-1] = x
            k -= 1
            steps += 1
    return lst,steps

print(insert_sort(lst))
