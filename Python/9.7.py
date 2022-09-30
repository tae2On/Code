import string 
src_str = string.ascii_uppercase + string.ascii_lowercase

data = str(input('문장을 입력하시오 : '))
move = int(input('이동시킬 칸 수를 입력하시오 : '))
dst_str = ''

for i in data :
    if (i.isalpha()):
        if (src_str.index(i) + 3 < len(src_str)):
            dst_str += src_str[src_str.index(i) + 3]
        else:
            dst_str += src_str[3 -(len(src_str) - src_str.index(i))]
    else:
        dst_str += i

print('암호화된 문장 :', dst_str)