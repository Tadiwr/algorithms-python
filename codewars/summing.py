def summation(num: int):
    if num == 1: return 1
    return num + summation(num - 1)


print(summation(5))