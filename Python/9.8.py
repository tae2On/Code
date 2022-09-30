data = str(input('문장을 입력하시오 :   '))

english = ' ' 
number = ' '
enum = ' ' 

for i in data : 
    if (i in ("\".\'/,><?!@#$%^&*()_;:-+=~`")):
        data = data.replace(i, '')
word = data.split()
 
for i in word : 
    if (i.isalpha()): 
        english = english + i
    elif (i.isdigit()):
        number = number + i
    elif (i.isalnum()): 
        enum = enum + i

print('영문 단어 : ', english)
print('숫자 : ', number)
print('영문자 + 숫자 : ', enum)