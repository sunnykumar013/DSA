class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Reverse:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node

            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node


    def reverseList(self):
        curr_node = self.head
        prev = None
        while curr_node != None:
            nxt = curr_node.next
            curr_node.next = prev
            prev = curr_node
            curr_node = nxt

        self.head = prev

    def tarversal(self):
        curr_node = self.head

        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next



if __name__ == "__main__":
    obj1 = Reverse()

    obj1.append(1)
    obj1.append(2)
    obj1.append(4)
    obj1.reverseList()
    obj1.tarversal()
