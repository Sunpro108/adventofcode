import numpy as np
import time

def STPA(serial_num):
    array_pos = np.zeros((300,300,2),dtype = int)
    array_pos[:,:,0] = np.arange(1,301)
    array_pos[:,:,0] = array_pos[:,:,0].T
    array_pos[:,:,1] = np.arange(1,301)
    array_pos[:,:,0] += 10
    total_array = ((array_pos[:,:,0]*array_pos[:,:,1] + serial_num)*array_pos[:,:,0])//100%10-5
    array_pos[:,:,0] -= 10
    return array_pos,total_array

def findLSTP(serial_num,size=3):
    array_pos,total_array = STPA(serial_num)
    array_pos = array_pos.reshape((300*300,2))
    list_stp = list(map(lambda p:total_array[p[0]-1:p[0]-1+size,p[1]-1:p[1]-1+size].sum(),array_pos))
    return array_pos[list_stp.index(max(list_stp))]

def flstp(total_array,array_pos,size):
    list_stp = []
    array_pos = array_pos[0:301-size,0:301-size].reshape(((301-size)*(301-size),2))
    for p in array_pos:
        list_stp.append(total_array[p[0]-1:p[0]-1+size,p[1]-1:p[1]-1+size].sum())
    pos_max = array_pos[list_stp.index(max(list_stp))]
    return max(list_stp),pos_max
	
def findLSTPAnySize(serial_num):
    array_pos,total_array = STPA(serial_num)
    list_v = [];list_p=[]
    for i in range(1,301):
        print(i,':',end=' ')
        time_start = time.time()
        r = flstp(total_array,array_pos,i)
        list_v.append(r[0])
        list_p.append(r[1])
        time_end = time.time()
        print(time_end-time_start)
    index_max = list_v.index(max(list_v))
    pos_max = list(list_p[index_max])
    pos_max.append(index_max+1)
    return pos_max
		
if __name__ == '__main__':
    time_start = time.time()
    serial_num = 3628
    print(findLSTP(serial_num,size=3))
    time_end = time.time()
    print('time:',time_end-time_start)
    time_start = time.time()
    pos_max = findLSTPAnySize(serial_num)
    time_end = time.time()
    print('2 time:',time_end-time_start)
    print(pos_max)















