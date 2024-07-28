"""你家猫猫打架的模拟"""


class Cat:

    def __init__(self, cat_name, cat_age, cat_arm):
        self.name = cat_name
        self.age = cat_age
        self.arm = cat_arm

    def attack(self):
        print("打你" * self.arm)

    def attackplus(self):
        self.arm += 1


# 父类在子类前,切子类括号内置顶父类的名臣


class CyberCat(Cat):
    # 子类继承父类,调用子类init再调用父类init
    def __init__(self, cat_name, cat_age, cat_arm):
        super().__init__(cat_name, cat_age, cat_arm)
        self.electric = 100

    def eco(self):
        print(self.electric * 0.1)

    def attackplus(self):
        self.electric += 1
