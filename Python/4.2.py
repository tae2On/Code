def print_number(a, b, c):
    data = list(map(int, input("세 정수를 입력하시오 :").split()))

    if (a >= b):
        if (b >= c):
            first = a 
            second = b 
            third = c
        elif (c >= b): 
            first = a 
            second = c
            third = b 
    elif (b >= a): 
        if (a >= c):
            first = b
            second = a 
            third = c
        elif (c >= a): 
            first = b
            second = c
            third = a
    elif (c >= a): 
        if (a >= b):
            first = c
            second = a 
            third = b
        elif (b >= a): 
            first = c
            second = b
            third = a

    return (first, second, third)