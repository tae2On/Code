data = int(input("정수를 입력하시오 : "))

if (data % 2 == 0):
    print (data, "는(은) 2(으)로 나누어집니다.")
else : 
    print (data, "는(은) 2(으)로 나누어지지 않습니다.")

if (data % 3 == 0):
    print (data, "는(은) 3(으)로 나누어집니다.")
else : 
    print (data, "는(은) 3(으)로 나누어지지 않습니다.")

if (data % 3 == 0 and data % 2 == 0):
    print (data, "는(은) 2와(과) 3 모두로 나누어집니다.")
else : 
    print (data, "는(은) 2와(과) 3 모두로 나누어지지 않습니다.")
