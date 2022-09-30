a = 'ABCD'
b = '1234'
new_str1 = ' '
new_str2 = ' '

for i in range(len(a)): 
    new_str1 = new_str1 + a[i] + b[i] 
for i in range(len(a)): 
    c = b[::-1]
    new_str2 = new_str2 + a[i] + (c[i])

print('a = ', a)
print('b = ', b)
print('new_str1 = ', new_str1)
print('new_str2 = ', new_str2)