class Pet:
    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color

    def speak(self):
        print("I dont know")

    def __getattr__(self, item):#when we want to get property that doesn't exist
        print('__getattr__')
        return False # Default value

    def __getattribute__(self, item):#when we get property that does exist
        print('__getattribute__',item)
        return object.__getattribute__(self,item)

    def __setattr__(self, key, value):
        print('__setattr__', key, value)
        return object.__setattr__(self, key, value)

    def __delattr__(self, item):
        print('__delattr__', item)
        object.__delattr__(self, item)
class Dog(Pet):
    def speak(self):
        print("Bark")
class Cat(Pet):
    def speak(self):
        print("Meow")
class Fish(Pet):
    def speak(self):
        print("Blub")
class Bear(Pet):
    def attack(self):
        print("ATTACK")

class Monostate:
    __shared_attr = {
        'name':"vlad",
        'data':{},
        'id':0
    }
    def __init__(self):
        self.__dict__ = self.__shared_attr

class Person:
    def __init__(self,name,age):
        self.__name = name
        #self.__age = age
        self.age = age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,age):
        self.verify_age(age)
        self.__age = age
    @staticmethod
    def verify_age(age):
        if not 16 <= age <= 30:
            raise ValueError("age can be only between 30 and 16")


class ReadIntX:
    def __set_name__(self, owner, name):
        self.name = '_' + name
    def __get__(self, instance, owner):
        return getattr(instance,self.name)

class Integer:
    def __set_name__(self, owner, name):
        self.name = '_' + name
    def __get__(self, instance, owner):
        return getattr(instance,self.name)
    def __set__(self, instance, value):
        setattr(instance,self.name,value)
class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()
    xr = ReadIntX()
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
class Singletone:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
        return cls.__instance
    def __init__(self,user,password,code):
        self.user = user
        self.password = password
        self.code = code
    def __del__(self):
        self.__instance = None
    def open(self):
        print(f"database open user - {self.user} password - {self.password} code - {self.code}")
class Counter:
    def __init__(self):
        self.__counter = 0
    def __call__(self, *args, **kwargs):
        print(self.__counter)
        self.__counter += 1
        return  self.__counter

class StringStriper:
    def __init__(self,chars):
        self.__chars = chars
    def __call__(self, *args, **kwargs):
        if not type(args[0]) is str:
            raise TypeError("Please use string, not %s"%(type(args[0])))
        return  args[0].strip(self.__chars)
class FuncDecoratorTest:
    def __init__(self,func):
        self.__fn = func
    def __call__(self,value, *args, **kwargs):
        return self.__fn(value) - self.__fn(value-1)
@FuncDecoratorTest
def decorator_func(value):
    print(f'decorator func valie - {value}')
    return value * value
class Player:
    def __init__(self,name,data):
        self.name = name
        self.data = data
    def __repr__(self):#debug
        return f'///{self.__class__} ///  {self.name}////'
    def __str__(self):#user friendly
        return f'///{self.__class__}////'
    def __len__(self):
        return len(self.data)
    def __abs__(self):
        print(self.data)
        return list(map(abs,self.data['Position']))
        #return len()

class Timer:
        def __init__(self, time):
            self.time = time

        def __add__(self, other):
            value = other
            if type(other) == type(self):#can be self.__class__:
                value = other.time
            self.time += value
            return self
        def __radd__(self, other):
            return self + other
        def __iadd__(self, other):
            self.time += other
            return self
def first_part():
    cat = Cat('vlad', 18, 'black')
    cat.speak()
    dog = Dog('vlad', 18, 'black')
    dog.speak()
    bear = Bear('vl', 12, 'd')
    bear.attack()
    print(bear.a)
    bear.name
    del bear.name
def second_part():
    me = Monostate()
    me2 = Monostate()
    me3 = Monostate()
    print(me.__dict__)
    print(me2.__dict__)
    print(me3.__dict__)
    me3.name = 'bad_vlad'
    print(me.__dict__)
    print(me2.__dict__)
    print(me3.__dict__)
def third_part():
    me = Person('vlad',16)
    #me.age = 10
def fourth_part():
    point1 = Point3D(1,2,4)
    point2 = Point3D(1,3,6)

    print(point1.__dict__)
    print(point2.__dict__)

    new_point = Point3D(1,2,3)
    new_point.xr = 1
    new_point.__dict__['x'] = 10
    print(new_point.__dict__)
    print(new_point.x)
    new_point.x = 15
    print(new_point.__dict__)
    print(new_point.x)
    pass
def part_5():
    db = Singletone('vlad','123532',3131)
    db2 = Singletone('avlad', '21312123532', 3131)
    print(id(db2),id(db))
    db.open()
def part_6():
    c = Counter()
    c()
    c()
    c()
    c()
    striper = StringStriper("abcd")
    print(striper("Vlad"))
    print(decorator_func(990))
def part_7():
    opponent = Player('gk',{'Position':(13,-99)})
    print(opponent)
    print(repr(opponent))
    print(len(opponent))
    print(abs(opponent))
    timer = Timer(12)
    print(timer.time)
    timer += 200 + 100
    timer = timer + 10 + 10 + 10 + 243
    timer2 = Timer(1000)
    timer += timer2
    print(timer.time)
    timer = 100 + timer#radd
    timer += 100 #iadd
    print(timer.time)
def main():
    first_part()
    second_part()
    third_part()
    fourth_part()
    part_5()
    part_6()
    part_7()
if __name__ == '__main__':
    main()
    pass
