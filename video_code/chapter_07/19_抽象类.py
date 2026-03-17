from abc import ABC,abstractmethod

# 【抽象类】是一种不能直接实例化的类，它通常作为“规范”，让子类继承，并实现其中未定义的【抽象方法】
# MustRun类一旦继承了ABC类，那么他就已经是抽象类了
class MustRun(ABC):
    @abstractmethod
    def run(self):
        pass
class Person(MustRun):
    def __init__(self,name,age,gender):
        self.name = name

    def run(self):
        pass