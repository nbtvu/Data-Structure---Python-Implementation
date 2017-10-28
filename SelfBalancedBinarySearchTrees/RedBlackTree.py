
class RBNode(object):
    val = None
    color = None # 0 1 <=> Black Red
    left = None
    right = None
    parents = None

    def __init__(self, val = None, color = 0):
        self.val = val
        self.color = color

class RBTree(object):
    root = RBNode()
