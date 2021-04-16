def calc(a, b):
    sum = a + b
    difference = a - b
    multiplication = a * b
    division = a / b

    my_list = [sum, difference, multiplication, division]

    for x in range(0, len(my_list)):
        sum = sum + my_list[x]

    print(sum)

calc(3,4)
