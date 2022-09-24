data = [] 

for alpabet in ['A', 'B', 'C']:
    data.append(alpabet) 
    for number in ['1', '2']: 
        data.append(alpabet*number)

print(data)