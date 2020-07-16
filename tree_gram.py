import numpy
import copy
class tree:
    def __init__(self,node):
        self.root=node
class treenode:
    def __init__(self,type,content=''):
        self.childs=[]
        self.content=content
        self.type=type
    def is_leaf(self):
        if len(self.childs)==0:
            return True
        else:
            return False
    def extends(self,tokens):
        for token in tokens:
            self.childs.append(token)
    def show(self):
        print(self.type)
        for node in self.childs:
            node.show()
    def equal(self,other):
        if self.type!=other.type:
            return False
        if len(self.childs)!=len(other.childs):
            return False
        for c1,c2 in zip(self.childs,other.childs):
            if c1.equal(c2)==False:
                return False
        return True
def issame(left,right):
    if len(left)!=len(right):
        return False
    for left1,right1 in zip(left,right):
        if not left1.equal(right1):
            return False
    return True
def isin(left,lefts):
    for item in lefts:
        if issame(left,item):
            return True
    return False
left_state=[]
tokens=['命令','连接词','命令','命令']
file=open("./grammars.txt",'r',encoding='utf-8').readlines()
grammars=[]
for line in file:
    line=line.strip()
    tokenss=line.split()
    grammars.append(tokenss)
print(grammars)
# grammars=[["S","VP","N"],["VP","N","V"]]
#我们采用移位规约+递归回溯法，由下至上解析
left=[]
remain=copy.deepcopy([treenode(token) for token in tokens])
print([item.type for item in remain])
# remain[1]=9
# print(tokens)
trees=[]
def alltree(left,remain):
    left_state.append(left)
    isfinish = False
    for i in range(len(left)):
             # if isfinish: break
             for j in range(i,len(left)):
                 # if isfinish:break
                 span=left[i:j+1]
                 for gram in grammars:
                     print(tuple([node.type for node in span]))
                     print(tuple(gram[1:]))
                     if tuple([node.type for node in span])==tuple(gram[1:]):
                         print('add new')
                         newnode=treenode(gram[0])
                         newnode.extends(span)
                         left1=copy.deepcopy(left[:i]+[newnode]+left[j+1:])
                         if not isin(left1,left_state):
                            alltree(left1, copy.deepcopy(remain))
                            isfinish=True
    if len(remain) > 0:
             # if isfinish:return None
             # else:
                 left.append(remain[0])
                 # print('dsd')
                 # print([item.type for item in left])
                 remain=remain[1:]
                 alltree(left, remain)
    else:
                 # if isfinish:return None
                 # else:
                     if len(left)>1:
                         print("failed")
                         return None
                     else:
                         if(left[0].type == 'S'):
                             print("success")
                             trees.append(left[0])
                         else:
                             print("failed")
                             return None
alltree(left,remain)
print(len(trees))
for tree in trees:
    tree.show()
# print(trees[0].equal(trees[1]))
# while(1):
#     isfinish = False
#     for i in range(len(left)):
#              if isfinish: break
#              for j in range(i,len(left)):
#                  if isfinish:break
#                  span=left[i:j+1]
#                  for gram in grammars:
#                      # print(tuple([node.content for node in span]))
#                      # print(tuple(gram[1:]))
#                      if tuple([node.type for node in span])==tuple(gram[1:]):
#                          print('add new')
#                          newnode=treenode(gram[0])
#                          newnode.extends(span)
#                          left=left[:i]+[newnode]+left[j+1:]
#                          isfinish=True
#     if len(remain) > 0:
#          if isfinish:continue
#          else:
#              left.append(remain[0])
#              remain=remain[1:]
#              print(left)
#     else:
#              if isfinish:continue
#              else:
#                  if len(left)>1:
#                      print("failed")
#                      break
#                  else:
#                      if(left[0].type == 'S'):
#                          print("success")
#                      else:
#                          print("failed")
#                      break
# left[0].show()
