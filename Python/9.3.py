Alpabet = 0
alpabet =0
number = 0
special = 0

data = str(input("문자열을 입력하시오 : "))

for i in data:    
    if (i.isalpha()):
        if (i.islower()):
            Alpabet = Alpabet + 1
        else : 
            alpabet = alpabet + 1
    elif (i.isdigit()):
        number = number + 1
    else : 
        special = special + 1

print("대문자, 소문자, 숫자, 특수문자의 개수")
print("대문자 = ", Alpabet)
print("소문자 = ", alpabet)
print("숫자 = ", number)
print("특수문자 = ", special)