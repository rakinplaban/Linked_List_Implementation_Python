
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
   

class Linkedlist:
    def __init__(self):
        self.count = 0
        self.p = None
        

    def insertNodeFirst(self, val):
        node = Node(val)
        if self.count == 0:
            self.p = node
        else:
            temp = self.p
            node.next = temp
            self.p = node

        self.count += 1

    def insertNodeLast(self,val):
        node = Node(val)
        temp = self.p
        while temp.next is not None:
            temp = temp.next.next
        
        temp.next = node
        self.count += 1

    def insertNodeInside(self,target,val):
        node = Node(val)
        temp = self.p
        while temp.next is not None:
            if temp.val == target:
                break;
            temp = temp.next
        temp1 = temp.next
        temp.next = node
        node.next = temp1
        self.count += 1

    def deleteNodeFirst(self):
        if self.count == 0:
            print("Under flow!")

        else:
            temp = self.p
            self.p = temp.next
            del(temp)
            self.count -= 1

    def deleteNodeLast(self):
        if self.count == 0:
            print("Under flow!")
        else:
            temp = self.p
            while temp.next.next is not None:
                temp = temp.next.next
            if temp.next.next is None:
                del(temp.next)
                temp.next = None
            self.count -= 1

    def display(self):
        temp = self.p
        while temp is not None:
            print(temp.val,end=" ")
            temp = temp.next


l1 = Linkedlist()
l1.insertNodeFirst(12)
l1.insertNodeFirst(13)
l1.display()
print()
item = int(input())
l1.insertNodeFirst(item)
l1.display()
print()
litem = int(input())
l1.insertNodeLast(litem)
l1.display()
print()
mitem = int(input())
l1.insertNodeInside(13,mitem)
l1.display()
print("\nThe number of node is : ",l1.count)
l1.deleteNodeFirst()
l1.display()
print("\nThe number of node is : ",l1.count)
l1.deleteNodeLast()
l1.display()
print("\nThe number of node is : ",l1.count)