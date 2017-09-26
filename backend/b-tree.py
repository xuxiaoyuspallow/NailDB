class BPlusTreeNode(object):
    def __init__(self,keywords,num_keys,children=None,parent=None,is_leaf=False):
        """
        :param keywords:表示关键字及它们指向的孩子
        :param num_keys: 关键字个数,每个节点的子树数量等于这个值(在某些B+树实现中，子树数量为num_keys+1,随意选择一个即可)
        :param parent: 此节点的父节点 Object(BPlusTreeNode)
        :param is_leaf :是否为叶节点
        :param children ：当节点为内部节点时，其指向子树，当节点为叶子节点时
        """
        self.keywords = keywords
        self.num_keys = num_keys
        self.parent = parent

        self.is_leaf = is_leaf
        self.children = []


class BplusTree(object):
    def __init__(self, root):
        self.root = root

    def insert(self, value):
        pass

    def delete(self, value):
        pass

    def search(self, value):
        pass

    def display(self):
        children = self.root.children
        while children:



if __name__ == '__main__':
    n1 = BPlusTreeNode([1],3)

