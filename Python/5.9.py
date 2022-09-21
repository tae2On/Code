data = 1
count = 0 
number = []

while True : 
    data = int(input("정수를 입력하시오 : "))

    if (data > 0): 
        count = count + 1    
        number.append(data) 
    elif (data == - 99): 
        break

number.sort(reverse = True)

print(count, "개의 유효한 정수 중 가장 큰 정수는", number[0], "이고, 가장 작은 정수는", number[count-1])