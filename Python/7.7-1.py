fruit_list = ['banana', 'orange', 'kiwi', 'apple', 'melon']

max_list = []

for i in fruit_list: 
    if (not max_list or len(i) > len(max_list[0])): 
        max_list.clear()
        max_list.append(i)
    elif (len(i) == len(max_list[0])):
        max_list.append(i)

for n in max_list: 
    fruit_list.remove(n)

print('가장 길이가 긴 문자열 : ', max_list)
print('fruit_list = ', fruit_list)