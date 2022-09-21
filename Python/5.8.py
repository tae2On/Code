while True:
    data = str(input("정수를 입력하시오 : "))
    print(data)
    data_list = list(data)
    data_list.reverse() 
    data_list = ''.join(data_list)

    if (data == data_list):
        print(data, '은(는) 거꾸로 정수입니다.')
    elif (data == '-99'): 
        print('프로그램을 종료합니다.')
        break
    else :
        print(data, '은(는) 거꾸로 정수가 아닙니다.') 