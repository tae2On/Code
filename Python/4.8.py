print("1)덧셈 2)뺄셈 3)곱셈 4)나누셈")
while True :
    data = int(input("어떤 연산을 원하는지 번호를 입력하세요: "))

    if ( 0 < data < 5 ): 
        a, b = map(float, input("연산을 원하는 숫자 두개를 입력하세요: ").split())

        if (data == 1): 
            print(a, "+", b, "=", a + b)
        elif (data == 2): 
            print(a, "-", b, "=", a - b)
        elif (data == 3):
            print(a, "*", b, "=", a * b) 
        elif (data == 4): 
            print(a, "/", b, "=", a / b) 

    else : 
        print("잘못 입력하였습니다.")