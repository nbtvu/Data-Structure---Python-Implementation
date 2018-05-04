from threading import Lock


class DoubleLinkedNode(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prevNode = None
        self.nextNode = None


class Queue(object):
    def __init__(self):
        self._pHead = None
        self._pTail = None

    def pushHead(self, newNode):
        newNode.prevNode = newNode.nextNode = None
        if self._pHead is None:
            self._pHead = newNode
            self._pTail = newNode
        else:
            newNode.nextNode = self._pHead
            self._pHead.prevNode = newNode
            self._pHead = newNode

    def pushTail(self, newNode):
        newNode.prevNode = newNode.nextNode = None
        if self._pTail is None:
            self._pHead = newNode
            self._pTail = newNode
        else:
            newNode.prevNode = self._pTail
            self._pTail.nextNode = newNode
            self._pTail = newNode

    def removeNode(self, node):
        if self._pHead == self._pTail == node:
            self._pHead = self._pTail = None
        elif node == self._pHead:
            self._pHead = self._pHead.nextNode
            self._pHead.prevNode = None
        elif node == self._pTail:
            self._pTail = self._pTail.prevNode
            self._pTail.nextNode = None
        else:
            prv = node.prevNode
            nxt = node.nextNode
            prv.nextNode = nxt
            nxt.prevNode = prv
        node.prevNode = node.nextNode = None

    def popTail(self):
        tail = self._pTail
        self.removeNode(self._pTail)
        return tail


class LRUCache(object):
    def __init__(self, max_size=1000000):
        self._max_size = max_size
        self._queue = Queue()
        self._hash_map = {}
        self._size = 0
        self._mutex = Lock()

    def put(self, key, val):
        res = True
        self._mutex.acquire()
        try:
            newNode = DoubleLinkedNode(key, val)
            self._hash_map[key] = newNode
            self._queue.pushHead(newNode)
            if self._size == self._max_size:
                tail = self._queue.popTail()
                del self._hash_map[tail.key]
            else:
                self._size += 1
        except:
            res = False
        self._mutex.release()
        return res

    def get(self, key):
        self._mutex.acquire()
        val = None
        try:
            node = self._hash_map.get(key, None)
            if node is not None:
                self._queue.removeNode(node)
                self._queue.pushHead(node)
                val = node.val
        except:
            pass
        self._mutex.release()
        return val


my_cache = LRUCache(3)

my_cache.put(1, "hello")
my_cache.put(2, "hi")
my_cache.put(3, "bye")
my_cache.put(4, "day")
my_cache.put(5, "night")
print(my_cache.get(3))
print(my_cache.get(1))
print(my_cache.get(3))
print(my_cache.get(4))
print(my_cache.get(3))
