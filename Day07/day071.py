# -*- utf-8 -*-
import re
from functools import reduce

# read the data
f = open('input.txt','r')
ins = f.readlines()

# 
def parsorInput(inp):
    pa = 'Step (\w) must be finished before step (\w) can begin.'
    step = re.findall(pa,inp)
    return step[0]
def getDictSteps(ins):
    listSteps = list(map(parsorInput,ins))
    ## 记录表
    setSteps = set([])
    setBefored = set([])
    dictSteps = {}
    dictRely = {}
    for step in listSteps:
        #
        setSteps.add(step[0])
        setBefored.add(step[1])
        #dict
        if step[0] in dictSteps:
            dictSteps[step[0]].append(step[1])
        else:
            dictSteps[step[0]] = [step[1]]
        #dictRely 
        if step[1] in dictRely:
            dictRely[step[1]].append(step[0])
        else:
            dictRely[step[1]]= [step[0]]
    # find the root 
    rootStep = sorted(list(setSteps - setBefored))
    return dictSteps,rootStep,dictRely

	
dictSteps,rootStep,dictRely = getDictSteps(ins)

list_ready = []
list_ready_pre = []
set_ready_pre = set([])
list_done = []
#将root添加到readylist
list_ready += rootStep

i = 1
while(not (len(list_ready) == 0 and len(set_ready_pre) == 0)):
#    print(i)
#     print('list_ready:',list_ready)
#     print('set_ready_pre',set_ready_pre)
    if len(list_ready) > 0:
        work = list_ready.pop(0)
        list_done.append(work)
        if work in dictSteps:
            for c in dictSteps[work]:
                if c not in list_done:
                    set_ready_pre.add(c)
    
#     print('list_done:',list_done)
#     print('list_ready:',list_ready)
    list_ready_pre = sorted(list(set_ready_pre))
#     print(list_ready_pre)
    for c in list_ready_pre:
        flag = True
        if c in dictRely:
            for r in dictRely[c]:
                if r not in list_done:
                    flag = False
                    break
        if flag:
            list_ready.append(c)
    list_ready = sorted(list_ready)
    set_ready_pre = set_ready_pre - set(list_ready) 
    i+=1
str_done = reduce(lambda m,n:m+n,list_done)

print(str_done)