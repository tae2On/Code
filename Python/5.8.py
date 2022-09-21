while True:
    data = str(input("정수를 입력하시오 : "))
    data_list = list(data)
    data_list.reverse() 
    print(''.join(data_list))

    if (data_list == data ):
        print( data, '은(는) 거꾸로 정수입니다.')
    elif (data_list == -99): 
        print('프로그램을 종료합니다.')
    else :
        print(data, '은(는) 거꾸로 정수가 아닙니다.') 