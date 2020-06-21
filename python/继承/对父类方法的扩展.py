# 1. 对父类方法进行重写
# 2. 在需要的位置使用super().父类方法  来调用父类方法的执行
# 3. 针对子类需求,编写子类特有的代码实现

class Animal(object):

    def eat(self):
        print('eating!')

class Dog(Animal):

    def bark(self):
        Animal.eat(self)
        # super().eat()
        print("汪汪叫")

class XiaoTian(Dog):

    def bark(self):
        # 1. 使用super调用父类方法的执行
        super().bark()
        # 2. 针对子类特有需求,编写代码
        print("神狗咆哮,嗷唔~")

xiao = XiaoTian()

xiao.bark()
