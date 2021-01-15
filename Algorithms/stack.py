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

def exp_to_lst(n):
    lst = []
    start_index = 0    
    end_index = 0      
    b_start = False
    for index, item in enumerate(n):
        if item.isdigit():
            if not b_start:  
                start_index = index    
                b_start = True         
        else:
            if b_start:  
                end_index = index     
                b_start = False       
                lst.append(n[start_index:end_index])   

            if item in ('+', '-', '*', '/', '(', ')'):    
                lst.append(item)

    if b_start:    
        lst.append(n[start_index:])
    return lst

map = {'+': 1, '-': 1, '*': 2,'/': 2}

def infix_exp_2_postfix_exp(NB):
    stack = Stack()
    NB_lst = exp_to_lst(NB)
    postfix_lst = []
    for item in NB_lst:
        if item.isdigit():
            postfix_lst.append(item)
        elif item == '(':
            stack.push(item)
        elif item == ')':
            while stack.top() != '(':
                postfix_lst.append(stack.top())
                stack.pop()
            stack.pop()
        else:
            while stack.size() != 0 and stack.top() in ("+-*/") and map[stack.top()] >= map[item]:
                postfix_lst.append(stack.top())
                stack.pop()
            stack.push(item)

    while stack.size() != 0:
        postfix_lst.append(stack.top())
        stack.pop()

    return postfix_lst




def c(op, op1, op2):
    if op == "*":
        return (op1 * op2)
    elif op == "+":
        return (op1+op2)
    elif op == "-":
        return (op1-op2)
    else:
        return (op1/op2)


def c_postfix(postfix):
    A = Stack()

    for i in postfix:
        if i.isdigit():
            A.push(int(i))
        else:
            numberA = A.top()
            A.pop()
            numberB = A.top()
            A.pop()
            result = c(i,numberB,numberA)
            A.push(result)
    
    return (A.top())

print(c_postfix("12+3+4+5+"))
print(c_postfix("12345*+*+"))

