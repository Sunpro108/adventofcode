f = open('input.txt','r')
#f = open('test.txt','r')
ins = f.read()

global list_data
list_data = list(map(int,ins.split()))
global counter_Total
counter_Total = len(list_data)


class Tree:
    def __init__(self,num_node,num_meta):
        self.num_node = num_node
        self.num_meta = num_meta
        self.node = []
        self.meta = []
    def add(self,index):
        while(len(self.node) != self.num_node):
#             print('add node')
#             print('index',index)
            if index < counter_Total:
                num_node = list_data[index]
            else:
                print('error: index out of range!')
                break
            index += 1
            if index < counter_Total:
                num_meta = list_data[index]
            else:
                print('error: index out of range!')
                break
            index += 1
            tree = Tree(num_node, num_meta)
            index = tree.add(index)
            self.node.append(tree)
        # node is fulled,add the meta data       
        for i in range(self.num_meta):
            if index < counter_Total:
                self.meta.append(list_data[index])
                index += 1
            else:
                print('error: index out of range!')
        return index
    def sum(self):
        sum_meta = 0
        if len(self.meta)>0:
            for data in self.meta:
                sum_meta += data
        if len(self.node)>0:
            for tree in self.node:
                sum_meta += tree.sum()
        return sum_meta
    def value(self):
        if len(self.node) == 0:
#             print(self.__str__())
            return self.sum()
        else:
            if len(self.meta) == 0:
                return 0
            value = 0
            for r in self.meta:
#                 print('meta_data:',r)
                rindex = r-1
                if rindex < len(self.node):
                    value += self.node[rindex].value()
            return value
    def __str__(self):
        return 'Num_node: %d, Num_meta: %d, counter_node: %d '%(self.num_node,self.num_meta,len(self.node))
		
list_tree = []
index = 0
sum_meta = 0
while( index < counter_Total):
    #print('index',index)
    num_node = list_data[index]
    index += 1
    num_meta = list_data[index]
    index += 1
    tree0 = Tree(num_node, num_meta)
    index = tree0.add(index)
    index += 1
    list_tree.append(tree0)
for tree in list_tree:
    sum_meta += tree.sum()
print(sum_meta)
print(tree0.value())