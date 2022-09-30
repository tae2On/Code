data = str(input("문자열을 입력하시오 : "))

Alpabet = ''
alpabet = ''

for i in data : 
    if (i >= 'A' and i <= 'Z'):
        Alpabet = Alpabet + i
    elif (i >= 'a' and i <= 'z'):
        alpabet = alpabet + i
    
print('수정된 문자열 : ', alpabet + Alpabet)