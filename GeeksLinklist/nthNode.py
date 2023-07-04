class Node:
    def __init__(self, data):
        self.data =data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def push(self,val):

        new_node = Node(val)
        new_node.next = self.head
        self.head =new_node

    def printlst(self,n):
        temp = self.head
        c =1
        while(temp):
            if c==n:
                print(temp.data)
            temp = temp.next
            c +=1



if __name__ == "__main__":

    lst1 = LinkList()
    lst1.push(1)
    lst1.push(10)
    lst1.push(30)
    lst1.push(14)
    lst1.printlst(2)