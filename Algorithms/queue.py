class Queue():
    # 初始化队列为空列表
    def __init__(self):
        self.queue1 = []
        

    # 判断队列是否为空，返回布尔值
    def is_empty(self):
        pass

    # 返回队列头部元素（即将出队的那个）
    def top(self):
        return(self.queue1[0])
        
    # 返回队列的大小
    def size(self):
        return len(self.queue1)

    # 把新的元素堆进队列里面（程序员喜欢把这个过程叫做入队…）
    def enqueue(self, item):
        self.queue1.append(item)

    # 把队列头部元素弹出来（程序员喜欢把这个过程叫做出队……）
    def dequeue(self):
        self.queue1.pop(0)


        
myqueue = Queue()
myqueue.enqueue(9)
myqueue.enqueue(7)
myqueue.enqueue(1)
myqueue.enqueue(8)
myqueue.enqueue(2)

print(myqueue.top())
myqueue.dequeue()

print(myqueue.top())
myqueue.dequeue()

print(myqueue.top())
myqueue.dequeue()