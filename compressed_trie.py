class Node(object):
    def __init__(self):
        self.children = {}
        self.str = ""
        self.val = None
        self.count = 0


class CompressedTrie(object):
    def __init__(self):
        self._root = Node()

    def put(self, key, value, override = True):
        keylen = len(key)
        idx = 0
        curNode = self._root
        while idx < keylen:
            nxtNode = curNode.children.get(key[idx], None)
            if nxtNode:
                j = 0
                while j < len(nxtNode.str) and idx + j < keylen:
                    if nxtNode.str[j] != key[idx + j]:
                        break
                    j += 1
                if j == len(nxtNode.str):
                    nxtNode.count += 1
                    curNode = nxtNode
                else:
                    newNode = Node()
                    newNode.count = nxtNode.count + 1
                    newNode.str = nxtNode.str[:j]
                    nxtNode.str = nxtNode.str[j:]
                    newNode.children[nxtNode.str[0]] = nxtNode
                    if idx + j > keylen:
                        newNode.val = value
                    curNode.children[key[idx]] = newNode
                    curNode = newNode
                idx += j
            else:
                newNode = Node()
                newNode.count = 1
                newNode.str = key[idx:]
                curNode.children[key[idx]] =  newNode
                curNode = newNode
                break
        if not override and curNode.val != None:
            return False
        else:
            curNode.val = value
        return True

    def get(self, key):
        node = self._get_node(key)
        if node:
            return node.val

    def autocomplete(self, keyword):
        keylen = len(keyword)
        idx = 0
        curNode = self._root
        while idx < keylen:
            nxtNode = curNode.children.get(keyword[idx], None)
            if nxtNode:
                j = 0
                while j < len(nxtNode.str) and idx + j < keylen:
                    if nxtNode.str[j] != keyword[idx + j]:
                        break
                    j += 1
                if j < len(nxtNode.str):
                    if idx + j == keylen:
                        curNode = nxtNode
                        keyword += nxtNode.str[j:]
                        break
                    return []
                curNode = nxtNode
                idx += j
            else:
                return []
        return self._traverse(curNode, keyword)

    def _get_node(self, key):
        keylen = len(key)
        idx = 0
        curNode = self._root
        while idx < keylen:
            nxtNode = curNode.children.get(key[idx], None)
            if nxtNode:
                j = 0
                while j < len(nxtNode.str) and idx + j < keylen:
                    if nxtNode.str[j] != key[idx + j]:
                        break
                    j += 1
                if j < len(nxtNode.str):
                    return None
                curNode = nxtNode
                idx += j
            else:
                return None
        return curNode

    def _traverse(self, node, curWord):
        matched = []
        if node.val is not None:
            matched.append(curWord)
        for ch in node.children:
            matched += self._traverse(node.children[ch], curWord + node.children[ch].str)
        return matched


my_data = CompressedTrie()

my_data.put("a", 6)
my_data.put("banana", 1)
my_data.put("na", 5)
my_data.put("nana", 3)
my_data.put("ana", 4)
my_data.put("anana", 2)

print(my_data.autocomplete("n"))
print(my_data.autocomplete("a"))
print(my_data.autocomplete("ba"))
print(my_data.get("nana"))
print(my_data.get("a"))
print(my_data.get("banana"))
print(my_data.get("ana"))
print(my_data.get("anana"))
print(my_data.get("ba"))
