class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def append(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while (last_node.next):
            last_node = last_node.next

        last_node.next = new_node


    def travelsal(self):

        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next


if __name__ == "__main__":
    obj1 = LinkList()
    obj1.append(30)
    obj1.append(20)
    obj1.append(8)
    obj1.travelsal()
