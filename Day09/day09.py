import re

f = open('input.txt','r')
# f = open('test.txt','r')
ins = f.readlines()

patn2 = '\d+'
result = re.findall(patn2,ins[0])
result =  list(map(int,result))

#day082
result[1] = result[1]*100

class Node():
    def __init__(self,num):
        self.prev = None
        self.next = None
        self.num = num

class BdclList():    
    def __init__(self,node):
        node.prev = node
        node.next = node
        self.current = node
    
    def insert(self,node,node_adding):
        node.next.prev = node_adding
        node_adding.next = node.next
        node_adding.prev = node
        node.next = node_adding
        
    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        return node
        
    def insert1(self,pos,node_adding):
        nodeAdded = self.getNodeAt(pos,True)
        self.insert(nodeAdded,node_adding)
    
    def remove1(self,pos):
        node = self.getNodeAt(pos,False)
        return self.remove(node),node.next
        
    def getNodeAt(self,pos,flag):
        node = self.current
        while(pos > 0):
            if flag:#clockwise 
                node = node.next
            else:
                node = node.prev
            pos -= 1
        return node    
    def setCurrent(self,node):
        self.current = node
    def getCurrent(self):
        return self.current

list_marble = []
list_scores = [0]*result[0]
marble = 0
node = Node(marble)
circle = BdclList(node)
marble += 1
while(marble < result[1]):
    if marble % 23 != 0:
        node = Node(marble)
        circle.insert1(1,node)
        circle.setCurrent(node)
    else:
        list_marble.append(marble)
        list_scores[marble%result[0]] = list_scores[marble%result[0]]+marble
        node,current_node = circle.remove1(7)
        circle.setCurrent(current_node)
        list_marble.append(node.num)
        list_scores[marble%result[0]] = list_scores[marble%result[0]]+node.num
    marble += 1

print(max(list_scores))







