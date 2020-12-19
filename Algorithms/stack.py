class Stack():
    # 初始化栈为空列表
    def __init__(self):
        self.data = []

    # 判断栈是否为空，返回布尔值
    def is_empty(self):
        pass

    # 返回栈顶元素
    def top(self):
        return self.data[-1]

    # 返回栈的大小
    def size(self):
        return len(self.data)

    # 把新的元素堆进栈里面（程序员喜欢把这个过程叫做压栈，入栈，进栈……）
    def push(self, item):
        self.data.append(item)

    # 把栈顶元素丢出去（程序员喜欢把这个过程叫做出栈……）
    def pop(self):
        self.data.pop()

mystack = Stack()
mystack.push(9)
mystack.push(7)
mystack.push(1)
mystack.push(8)
mystack.push(2)

print(mystack.top())
mystack.pop()
print(mystack.top())
mystack.pop()
print(mystack.top())
mystack.pop()
