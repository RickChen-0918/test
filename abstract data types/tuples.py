def tuples_problem4(lst):
    evens = 0
    for i in lst:
        sum = 0
        try:
            for k in i:
                sum += k
        except:
            sum += i
        if sum%2 == 0:
            evens += 1
    return evens





print(tuples_problem4([(1, 2), (5, 6, 7), (6, 9), (0), (), (3, 0)]))
