import re 

s = '문장 s : English = 89, Science = 90, Math = 92, History = 80'
print(s)
data = re.findall("\d+", s)

add = 0
average = 0

for i in data :
    if i.isnumeric():
        add = add + int(i)
        average = average + 1


print('총점 : ', add)
print('평균점수 : ', add / average)
