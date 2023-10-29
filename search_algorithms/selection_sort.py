lst = [5,3,2,7,6,3,8,1,2,3,3444]

min = lst[0]
index = 0
for i in range(len(lst)):
    if lst[i] < min:
        min = lst[i]
        index = i

A = [64, 25, 12, 22, 11]

for i in range(len(A)):
     
    # Find the minimum element in remaining
    # unsorted array
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
             
    # Swap the found minimum element with
    # the first element       
    A[i], A[min_idx] = A[min_idx], A[i]

print(min,index)
print(lst)