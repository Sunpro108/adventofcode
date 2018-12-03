f = open('input.txt','r')
freqc = list(map(int,f))

def findRepeatedFreq(freqc):
    seed = {}
    currentfreq = 0
    while(True):
        for line in freqc:
            currentfreq += line
            if currentfreq in seed:
                return currentfreq
            else:
                seed[currentfreq] = '1'

testlist1 = [3, 3, 4, -2, -4]				
assert findRepeatedFreq(testlist1) == 10, "testlist1Error"
testlist2 = [-6, 3, 8, 5, -6]
assert findRepeatedFreq(testlist2) == 5, "testlist2Error"

print(findRepeatedFreq(freqc))