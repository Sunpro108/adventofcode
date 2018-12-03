# 统计字符串中字符出现的次数
def countLetter(boxID):
    dictLetters = {}
    for c in boxID:
        dictLetters[c] = (dictLetters[c] + 1) if (c in dictLetters) else (1)
    return dictLetters

# 统计出现包含numTwo,nuThree
def CheckNum(dictLetters,numTwo,numThree):
    if 2 in dictLetters.values():
        numTwo += 1
    if 3 in dictLetters.values():
        numThree += 1
    return numTwo,numThree	

f = open('input.txt','r')
listDictLetters = list(map(countLetter,f))

numTwo = 0
numThree = 0
for dictLetters in listDictLetters:
    numTwo,numThree = CheckNum(dictLetters,numTwo,numThree)

print(numTwo*numThree)


