def make_bricks(small:int, big:int, goal:int) -> bool:
    return goal%5 <= small if goal//5 <= big else goal-5*big <= small


def AddDigits(num:int) -> int:
    while len(str(num)) > 1:
        num = sum([int(digit) for digit in str(num)])
    return num
