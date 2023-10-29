import random

def plinko(start_pos):
    position = start_pos
    money = [3500,350,3500,0,10000,0,3500,350,3500]
    for i in range(12):
        if i%2 == 0: 
            if position == 1:
                pass
            elif position == 9:
                position -= 1
            else:
                position -= random.randint(0,1)
        else:
            position += random.randint(0,1)
    
    return money[position-1]

avg_return = []
for k in range(9):
    total = 0
    for i in range(100000):
        total += plinko(k+1)
    avg_return.append(float("{:.2f}".format(total/100000)))
        
print(avg_return)

                
