import re
import numpy as np

### 读入数据
f = open('input.txt','r')

ins = f.readlines()

### 建立大布
fabric = np.zeros((1000,1000),dtype = np.int16)

pattern = re.compile('#([0-9]*) @ ([0-9]*),([0-9]*): ([0-9]*)x([0-9]*)')

for line in ins:
    result = list(map(int,re.findall(pattern, line)[0]))

    fabric[result[1]:result[1]+result[3],result[2]:result[2]+result[4]] +=1

print('day031: ',np.where(fabric>1)[0].shape[0])

for line in ins:
    result = list(map(int,re.findall(pattern, line)[0]))
    if fabric[result[1]:result[1]+result[3],result[2]:result[2]+result[4]].sum() == result[3]*result[4]:
        print('day032: ', result[0])
