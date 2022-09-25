data = str(input('문자열을 입력하세요 : '))
p = [x for x in data]

for i in range(len(p) - 1): 
    print(p[:data(i) + 1])

for i in range(len(p) + 1): 
    print(p[:data(i) - 1])
