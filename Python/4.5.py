import random
a = random.randint(0,9)
b = random.randint(0,9)
c = random.randint(0,9)
print(a, b, c)
data = list(map(int, input("세 복권번호를 입력하시오 : ").split()))
count = 0

for i in range(0,3):
    if (data[i] == a) :
        count = count + 1
    elif (data[i] == b) :
        count = count + 1
    elif (data[i] == c) :
        count = count + 1

if (count == 3):
    print("상금 1억원")
elif (count == 2): 
    print("상금 1천만원")
elif (count == 1): 
    print("상금 1만원")
else : 
    print("다음 기회에 ...")


