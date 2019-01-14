import re
from functools import reduce
import numpy as np

def move(array_points,step):
    index = 0
    list_var = []
    flag_no_message = True
    while(index < step):
        index += 1
        array_points[:,0] += array_points[:,1]
#         print(array_points)
        list_var.append(array_points[:,0].var())
        if len(list_var)>3 and list_var[-1] - list_var[-2] > 0 and list_var[-2] -list_var[-3]<0: 
            print('find the show after %d seconds!'%(index-1))
            array_points[:,0] -= array_points[:,1]
            flag_no_message = False
            break;
            
    if flag_no_message:
        print('did not find the message!')
        print(list_var)
    return list_var,array_points

def show(array_points):
    xy =  array_points[:,0]
    a = array_points[:,0,0]
    b = array_points[:,0,1]
    s = np.lexsort((b,a))
    xy = xy[s]
    widthmin = xy.T[0].min()
    widthmax = xy.T[0].max()
    heightmin = xy.T[1].min()
    heightmax = xy.T[1].max()
    xy_new = xy - [widthmin,heightmin]
    list_show = [['.']*(widthmax-widthmin+1)]*(heightmax-heightmin+1)
    array_show = np.array(list_show)
    for p in xy_new:
        array_show[p[1],p[0]] = '#'
    str_show = ''
    for ls in array_show:
        str_show += reduce(lambda m,n:m+n,ls)
        str_show += '\n'
    print(str_show)

# f = open('test.txt','r')
f = open('input.txt','r')
fline = f.readlines()
patn = '-*\d+'
list_points = []
for line in fline:
    result = re.findall(patn,line)
    point = list(map(int,result))
#     point = [(result[0],result[1]),(result[2],result[3])]
    list_points.append(point)
array_points = np.array(list_points)
array_points = array_points.reshape((array_points.shape[0],2,2))

list_var,array_points = move(array_points,1000000)

show(array_points)






