class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def __repr__(self):
        if self.nodeCount == 0:
            return "LinkedList: empty"
        s = ""
        curr = self.head
        while curr is not None:
            s += repr(curr.data)
            if curr.next is not None:
                s += " -> "
            curr = curr.next
        return s

    def getAt(self, pos):
        if pos <= 0 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    def traverse(self):
        if self.nodeCount == 0:
            return []
        curr = self.head
        length = self.nodeCount

        result = []
        while length > 0:
            result.append(curr.data)
            curr = curr.next
            length -= 1
        return result

    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode = self.head
            self.head = newNode
        else:
            # 맨끝이면 굳이 getAt 호출해서 tail 을 바로 prev로 세팅
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1

        return True

    def concat(self, L):
        self.tail.next = L.head

        # L 리스트가 유효한 경우만
        if L.tail:
            self.tail = L.tail
        self.nodeCount += L.nodeCount
