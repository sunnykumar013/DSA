class Node:
    def __init__(self, data):
        self.data =data
        self.next = None

class Linklst:

    def __init__(self):
        self.head =None


    def push(self,val):

        new_node = Node(val)
        print(new_node)
        new_node.next = self.head
        self.head = new_node

    def traversal(self):
        temp =self.head
        while(temp):

            print(temp.data)
            temp = temp.next


if __name__  == "__main__":
    obj1 = Linklst()
    obj1.push(31)
    obj1.push(23)
    obj1.traversal()

    # obj1.traversal()

