class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linklst:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

        # print(new_node.data)

    def printlst(self,search):
        temp = self.head
        while(temp):
            # print(temp.data)
            if(temp.data == search):
                print(temp.data, "is found")
                break
            temp =temp.next

    def lengthlst(self):
        temp = self.head
        count =0
        while(temp):
            # print(temp.data)
            count += 1
            temp =temp.next

        print(count)



if __name__ == "__main__":
    llist= Linklst()
    llist.push(10)
    llist.push(30)
    llist.push(11)
    llist.push(21)
    llist.push(14)

    llist.printlst(130)

    llist.lengthlst()

