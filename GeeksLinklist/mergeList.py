class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Merge:
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

    def traversal(self):
        curr_node = self.head

        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next

    def mergeList(self, curr_lst1, curr_lst2):

        # curr_lst1 , curr_lst2 = self.head, self.head
        dumy_node = Node(0)
        tail = dumy_node
        while curr_lst1 != None and curr_lst2 != None:
            if curr_lst1.data <= curr_lst2.data:
                tail.next = curr_lst1

                curr_lst1 = curr_lst1.next


            else:
                tail.next = curr_lst2

                curr_lst2 = curr_lst2.next
            tail = tail.next

        while curr_lst1 != None:
            tail= curr_lst1
            tail = tail.next
            curr_lst1 = curr_lst1.next

        while curr_lst2 != None:
            tail.next = curr_lst2
            tail = tail.next
            curr_lst2 = curr_lst2.next




if __name__ == "__main__":
    obj1 = Merge()
    obj2 = Merge()
    obj1.append(1)
    obj1.append(2)
    obj1.traversal()
    print()

    obj2.append(11)
    obj2.append(12)
    obj2.append(13)
    obj2.traversal()

    obj1.mergeList(obj1.head, obj2.head)
    print()
    obj1.traversal()


