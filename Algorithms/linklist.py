class Node(object):
	#节点类
    #功能：输入一个值data，将值变为一个节点
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList(object):
    def __init__(self, head = None):
        self.head = head
    def __len__(self):
        #功能：输入头节点，返回链表长度
        C = 0
        curr = self.head
        while curr is not None:
            C+=1
            curr = curr.next
        return C

    def print_all(self):
        # 功能：打印整个链表
        curr = self.head
        while curr is not None:
            print(curr.data, end='')
            print('->', end='')
            curr = curr.next
        print("\n")
        return
        
    def insertToFront(self,data):
        #功能：输入data，插入到头节点前，并更改为头节点
        #输出：当前头节点
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert(self,data, pos):
        #功能：输入data，插入到第pos个节点的位置上
        #输出：当前头节点
        new_number = Node(data)
        if pos == 0:
            new_number.next = self.head
            self.head = new_number
            return self.head  
        curr = self.head
        curr2 = self.head
        for i in range(0,pos):
            curr = curr.next
        new_number.next = curr
        for b in range(0,pos-1):
            curr2 = curr2.next
        curr2.next = new_number
        return self.head



        
        
    def append(self,data):
        #功能：输入data,作为节点插入到末尾
        new_node = Node(data)
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node

    def get(self, pos):
        #功能: 输入索引，返回指定索引处的结果
        curr = self.head
        if pos >= self.__len__():
            return("❌")
        else:
            for i in range(0,pos):
                curr = curr.next
        return curr



    def find(self,data):
        #功能：查找链表的节点data与data相同的节点
        curr = self.head
        while curr is not None:
            if curr.data == data:
                return curr
            curr = curr.next
        return ("✖️")

    def delete(self,pos):
        #删除节点
        if pos == 0:
            self.head = self.head.next
            return self.head
        curr = self.head
        for i in range(0,pos-1):
            curr = curr.next
        curr.next = curr.next.next
        return self.head
    
    def Reverse(self):
        none = None
        curr = self.head
        while curr != None:
            next = curr.next
            curr.next = none
            none = curr
            curr = next
        self.head = none
        
        return none













n2 = Node(1)
n3 = Node(2)
n5 = Node(4)
n2.next = n3
n3.next = n5
linkedlist = LinkedList(head=n2)
print(linkedlist.Reverse())
linkedlist.print_all()
