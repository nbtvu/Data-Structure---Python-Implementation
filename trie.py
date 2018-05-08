class Node(object):
    def __init__(self):
        # the value associated with keyword
        self.val = None
        # count is the number of keywords going through the node
        self.count = 0
        self.children = {}


class Trie(object):
    def __init__(self):
        self._root = Node()

    def put(self, key, value, override = True):
        keylen = len(key)
        idx = 0
        curNode = self._root
        while idx < keylen:
            nxtNode = curNode.children.get(key[idx])
            if nxtNode:
                curNode = nxtNode
            else:
                curNode.children[key[idx]] = Node()
                curNode = curNode.children[key[idx]]
            curNode.count += 1
            idx += 1
        if not override and curNode.val != None:
            return False
        else:
            curNode.val = value
        return True


    def get(self, key):
        node = self._get_node(key)
        if node:
            return node.val

    def remove(self, key):
        node = self._get_node(key)
        if not node:
            return False
        node.val = None
        keylen = len(key)
        idx = 0
        curNode = self._root
        while idx < keylen:
            nxtNode = curNode.children[key[idx]]
            nxtNode.count -= 1
            if nxtNode.count == 0:
                del curNode.children[key[idx]]
                break
            curNode = nxtNode
            idx += 1
        return True


    def autocomplete(self, keyword):
        node = self._get_node(keyword)
        if not node:
            return []
        return self._traverse(node, keyword)


    def _get_node(self, key):
        keylen = len(key)
        idx = 0
        curNode = self._root
        while idx < keylen:
            nxtNode = curNode.children.get(key[idx])
            if nxtNode:
                curNode = nxtNode
            else:
                return None
            idx += 1
        return curNode

    def _traverse(self, node, curWord):
        matched = []
        if node.val is not None:
            matched.append(curWord)
        for ch in node.children:
            matched += self._traverse(node.children[ch], curWord + ch)
        return matched


my_data = Trie()

my_data.put("a", 6)
my_data.put("banana", 1)
my_data.put("na", 5)
my_data.put("nana", 3)
my_data.put("ana", 4)
my_data.put("anana", 2)

my_data.remove("ana")
my_data.remove("nana")

print(my_data.autocomplete("n"))
print(my_data.autocomplete("a"))
print(my_data.get("nana"))
print(my_data.get("a"))
print(my_data.get("banana"))
print(my_data.get("ana"))
print(my_data.get("an"))
print(my_data.get("ba"))
