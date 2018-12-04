import re
import numpy as np
from functools import reduce

def parsorRecords(timestamps):
    pa = '\[([0-9]{4})-([0-9]{2})-([0-9]{2}) ([0-9]{2}):([0-9]{2})\] (Guard #(\d*)|falls|wakes)'
    tt = re.findall(pa,timestamps)[0]
    time = ""
    flag = 0
    guardID = None
    time = int(reduce(lambda x,y:x+y, tt[:5]))

    if tt[5] == 'wakes':
        flag = 1
    elif tt[5] == 'falls':
        flag = -1
    else:
        flag = tt[6]
    return [time,flag]
	
f = open('input.txt','r')
ins = f.read().splitlines()
	
listRecords = list(map(parsorRecords,ins))
listRecords.sort()	
	
dictGuard = {}
guardid = ''

startSleep = 0
endSleep = 0
for aa in listRecords:
    if aa[1] == -1:
        startSleep = aa[0]%100
    elif aa[1] == 1:
        endSleep = aa[0]%100
        dictGuard[guardid][-1][startSleep:endSleep] = 1
    elif aa[1] not in dictGuard:
        guardid = aa[1]
        dictGuard[guardid] = []
        meteTime = np.zeros(60)
        dictGuard[guardid].append(meteTime) 
    elif aa[1] in dictGuard:
        guardid = aa[1]
        meteTime = np.zeros(60)
        dictGuard[guardid].append(meteTime) 
for g in dictGuard:
    dictGuard[g] = np.array(dictGuard[g])

g = {guard:dictGuard[guard].sum() for guard in dictGuard}
# print(g)
sortedg = sorted(g.items(),key = lambda x:x[1],reverse=True)

s = dictGuard[sortedg[0][0]].sum(axis = 0)
	
print(np.where(s == s.max())[0][0] * int(sortedg[0][0]))

g = {guard:dictGuard[guard].sum(axis=0).max() for guard in dictGuard}
sortedg = sorted(g.items(),key = lambda x:x[1],reverse=True)
	
# dictGuard(sortedg[0])
s = dictGuard[sortedg[0][0]].sum(axis = 0)
print(np.where(s == s.max())[0][0] * int(sortedg[0][0])	)