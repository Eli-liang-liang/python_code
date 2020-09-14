class Dog():
    """一次模拟小狗的简单尝试"""
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")

dog1 = Dog("dog1", 1)
print(dog1.name)
# 位置实参
# dog2 = Dog("🐶", 5) 
# 关键字实参
dog2 = Dog(age=5, name="🐶")
print(dog2.name)
print(dog2.age)

dog1.sit()
dog2.sit()

dog3 = Dog(name = "doge", age = 10)
dog3.sit()
dog3.roll_over()
# 打印 dog3 的名字
dog3.name = "doge2"
# 修改 doge 的名字 为 doge2 ，再让它坐下打滚
dog3.sit()
dog3.roll_over()

Dog(name = "doge10", age = 10).sit()

class Solution:
    # def __init__(self):
    #     # 啥都没有
    def test(self):
        print("test class soluton")

Solution().test()
# print(Dog(dog2).sit())





# dog2 = Dog("dog2", 2)

