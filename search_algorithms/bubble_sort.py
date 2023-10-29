lst = [5,3,2,7,6,3,8,1,2,3,3444]

def bubble_sort(lst):
    steps = 0
    for i in range(len(lst)):
        sorted = True
        for k in range(len(lst)-i-1):
            if lst[k] > lst[k+1]:
                x = lst[k]
                lst[k] = lst[k+1]
                lst[k+1] = x
                steps += 1
                sorted = False
        if sorted:
            break
    return lst,steps

print(bubble_sort(lst))
