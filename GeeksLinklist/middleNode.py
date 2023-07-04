class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head =None

    def push(self,  val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def printlst(self):
        fast =self.head
        slow = self.head
        while(fast != None  and fast.next != None):
            slow =slow.next
            fast = fast.next.next
        
        print("middle element",slow.data)

if __name__ == "__main__":
    lst1 = LinkList()
    lst1.push(12)
    lst1.push(15)
    lst1.push(21)
    lst1.push(22)
    lst1.push(45)
    lst1.printlst()
