class Dog():    # Python中首字母大写的名称指的是类
    def __init__(self, name, age):    # 类中的函数称为方法，__init__是一种特殊的方法
        self.name = name    # 形参self必不可少，且必须位于其他形参之前。每个与类相关联的方法都自动传递实参self，它是一个指向实例本身的引用。
        self.age = age

    def sit(self):
        print(self.name.title() + ' is now sitting.')

    def roll_over(self):
        print(self.name.title() + ' rolled over.')


my_dog = Dog('willie', 6)
# Python先找到实例my_dog，再查找与这个实例相关联的属性name，age。
print('My dog\'s name is '+ my_dog.name.title() + '.')
print('My dog is ' + str(my_dog.age) + ' years old.')
# Python先找到实例my_dog，再查找方法sit(),roll_over()。
my_dog.sit()
my_dog.roll_over()


class User():
    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为用户对象绑定first_name，last_name，age三个属性
    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def describe_user(self):
        if self.gender == 'female':
            print('这是%s%s女士!' % (self.first_name, self.last_name))
        if self.gender == 'male':
            print('这是%s%s先生!' % (self.first_name, self.last_name))
        print('年龄为%d' % self.age)

    def greet_user(self):
        print('欢迎%s%s的到来！' % (self.first_name, self.last_name))


user1 = User('Ou', 'Zou', 'male', 23)
user2 = User('Mengya', 'Gong', 'female', 22)
user1.describe_user()
user2.describe_user()
user1.greet_user()
user2.greet_user()


class Car():
    # 给汽车类加一个随时间变化的总里程
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it')

    def update_odometer_reading(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("禁止把里程往回调!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


my_new_car = Car(year=2021, make='Audi', model='Q8')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.update_odometer_reading(150)
my_new_car.read_odometer()
my_new_car.update_odometer_reading(120)
my_new_car.read_odometer()
my_new_car.increment_odometer(50)
my_new_car.read_odometer()


# 创建子类的实例时，先把父类所有属性赋值
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        print('电瓶容量是 ' + str(self.battery_size))


my_tesla = ElectricCar('tesla', 'model s', 2021)
print(my_tesla.get_descriptive_name())
print(my_tesla.describe_battery())


class Pet():
    """宠物"""

    def __init__(self, nickname):
        self._nickname = nickname




class Dog(Pet):
    """狗"""

    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)


class Cat(Pet):
    """猫"""

    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)


def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()


if __name__ == '__main__':
    main()
