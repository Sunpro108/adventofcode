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

	
class Worker:
    def __init__(self):
        self.work = None
        self.counter = 0
    
    def getWork(self,list_ready):
        if self.work == None:
            if len(list_ready) > 0:
                self.work = list_ready.pop(0)
                self.counter = 1
        else:
            self.counter += 1
        return list_ready

    def checkWork(self,list_done,dictSteps,set_ready_pre):
        if self.work != None:
            if self.counter == (ord(self.work) - ord('A') + 61):
                list_done.append(self.work)
                if self.work in dictSteps:
                    for c in dictSteps[self.work]:
                        if c not in list_done:
                            set_ready_pre.add(c)
    #             list_ready_pre += dictSteps[self.work]
                self.work = None
                self.counter = 0
        return list_done,set_ready_pre
	
	
def workerFactory(n):
    list_workers = []
    for i in range(n):
        list_workers.append( Worker())
    return list_workers
	
dictSteps,rootStep,dictRely = getDictSteps(ins)

list_ready = []
list_ready_pre = []
set_ready_pre = set([])
list_done = []
#将root添加到readylist
list_ready += rootStep


# 生成workers：
num_worker = 5
list_workers = workerFactory(num_worker)



## 循环
debug = False
i = 0
worksleepflag = False
while ( not(len(list_ready) == 0 and worksleepflag)):
    
#    print('step:',i)
    # 取数
    for worker in list_workers:
        list_ready =  worker.getWork(list_ready)
        
    # 检验worker的状态
    sflag = True
    for worker in list_workers:
        list_done,set_ready_pre = worker.checkWork(list_done,dictSteps,set_ready_pre)
        sflag = sflag and (worker.work == None)
    worksleepflag = sflag
    ## 排除已经done的ready_pre
    list_ready_pre = sorted(list(set_ready_pre))
    if debug:
        print(list_done,list_ready_pre)
    # 检验list_ready_pre的状态,结合list_done的内容，将真正准备好的添加到list_ready
    if len(list_ready_pre) > 0:
        for c in list_ready_pre:
            if c in list_done:
                continue
            flag = True
            for d in dictRely[c]:
#                 print(d)
                if d not in list_done:
                    flag = False
                    break
            if flag:
                list_ready.append(c)
        if debug:
            print(list_done)
            print(list_ready)
        set_ready_pre = set(list_ready_pre)-set(list_ready)
    i += 1

print(i)
