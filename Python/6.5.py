def cel2fah(cel): 
    fah = (9/5) * cel + 32
    return fah 

for i in range (0, 51, 10):
    fah = cel2fah(i)
    print ("섭씨온도 : ", i, ", 화씨온도 : ", fah)