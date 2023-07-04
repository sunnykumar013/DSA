class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None

    def push(self,val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def detectLoop(self):
        slow = self.head
        fast = self.head

        while(slow != None and fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                count =1
                while(slow != fast):
                    count +=1
                return count
        return 0


if __name__ == "__main__":
    llist = LinkList()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(10)
    llist.head.next.next.next = llist.head
    check = llist.detectLoop()
    if check == True:
        print("Loop detected",check)

    else:
        print("loop not detected")
