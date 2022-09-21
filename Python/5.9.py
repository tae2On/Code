data = 1
count = 0 
number = []

while True : 
    if (data > 0): 
        data = int(input("정수를 입력하시오 : "))
        number.append(data)        
        count = count + 1    
    elif (data == -99): 
        break 
    
a = data 
b = data 
while (data > 0):
    if (a > data):
        data = a 
    
while (data > 0):
    if (b < data):
        data = b    

print(count, "개의 유효한 정수 중 가장 큰 정수는", a, "이고, 가장 작은 정수는", b)