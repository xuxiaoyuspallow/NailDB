class Company(object):
    def __init__(self,value):
        self.value = value
        self.children = []
"""
    1
  /   \
  2    3    6
 / \    /  \
7  8     4    5
{1:[2:[],3:[4:[],5:[]]}
{1:{2:{},3:{4:{},5:{}}}
"""
c1 = Company(1)
c2 = Company(2)
c3 = Company(3)
c4 = Company(4)
c5 = Company(5)
c6 = Company(6)
c7 = Company(7)
c8 = Company(8)
c9 = Company(9)
c10 = Company(10)
c11 = Company(11)

c1.children.extend([c2,c3,c6])
c3.children.extend([c4,c5])
c2.children.extend([c7,c8])
c6.children.extend([c9,c10])
c5.children.extend([c11])


def test():
    res = {}
    def help(father,company,level):
        if not res.get(level):
            res[level] = []
        if father:
            res[level].append({father.value:company.value})
        else:
            res[level].append({0: company.value})
        level += 1
        for c in company.children:
            help(company,c,level)
    help(0,c1,0)
    result = {}
    key = []
    for i in range(len(list(res))):
        if i == 0:
            result[list(res[0][0].values())[0]] = [{list(k.values())[0]:[]}for k in res[1] if
                                                   list(k.keys())[0] == list(res[0][0].values())[0]]
            key.append(1)
        for j in range(len(res[i])):
            result[list(res[i][j].values())[0]] = [{list(k.values()): []} for k in res[i+1] if list(k.keys()) == list(res[i][j].values())[0]]

    return res

test()