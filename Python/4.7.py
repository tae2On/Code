import imp


import random 
a = random.randint(1,100)
b = random.randint(1,100)

print (a, "+", b, "=")
data = int(input("a와 b의 합 = " ))
x = a + b

if (data == x): 
    print ( "'잘했어요!'")
else: 
    print("정답은", x, "입니다.")
