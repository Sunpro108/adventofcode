import numpy as np

def parsorCoord(coordinate):
    return list(map(int,coordinate.split(', ')))
	
def drawArea(n,m):
    area = np.zeros((m,n,2))
    for i in range(m):
        area[i,:,1] = i # 行
    for j in range(n):
        area[:,j,0] = j # 列
    return area

f = open('input.txt','r')
ins = f.readlines()	
	
arrCoord = np.array(list(map(parsorCoord,ins)),dtype=np.int16)
p = arrCoord.shape[0]

right = arrCoord[:,0].max()
bottom = arrCoord[:,1].max()
m = bottom + 1
n = right + 1

listDists =[]
for coord in arrCoord:
    area = drawArea(n,m)
    dist = abs(area - coord).sum(axis = 2)
#     print(dist.shape)
    listDists.append(dist)
listDists = np.array(listDists)

nums = listDists.T.reshape((listDists.shape[1]*listDists.shape[2],listDists.shape[0]))
# print(nums)
print(nums.shape)
nums2 = [np.where(nums[i] == nums[i].min())[0] for i in range(nums.shape[0])]
# print(nums2)
listdist = []
for nums in nums2:
    if nums.shape[0]>1:
        listdist.append(-1)
    else:
        listdist.append(nums[0])
listnums = np.array(listdist).reshape((right+1,bottom+1))

listBJ = np.array([])
listBJ = np.append(listBJ,listnums[0])
listBJ = np.append(listBJ,listnums[-1])
listBJ = np.append(listBJ,listnums[:,0])
listBJ = np.append(listBJ,listnums[:,-1])
setBJ = set(listBJ)

arrCount = {}
for c in range(arrCoord.shape[0]):
    if c not in setBJ:
        arrCount[str(c)] = np.where(listnums==c)[0].shape[0]
print(arrCount)
sortedCount = sorted(arrCount.items(),key = lambda x:x[1],reverse=True)
print(sortedCount[0][1])

## Day062
print(np.where(listDists.sum(axis=0)<10000)[0].shape[0])










































