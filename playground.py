def add(*args):
    number = 0
    for num in args:
        number += num
    # print(number)
    return number

print(add(3,5,6))
