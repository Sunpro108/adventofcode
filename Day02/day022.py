

### 返回相同的字符
def commonLetters(str1, str2):
    # 长度一定相同，不检查
    i = 0
    countDiffer = 0
    str0 = ''
    for c in str1:
        if c == str2[i]:
            str0+=c
        i+=1
    if len(str0) == (len(str1)-1):
        return str0
    else:
        return None

f = open('input.txt','r')
ins = f.read().splitlines()

i = 0
t = len(ins)
#print(t)
for i in range(t):
    for j in range(i+1,t):
        result = commonLetters(ins[i],ins[j])
        if result is not None:
            print(i,j,result)
        j+=1
    i+=1