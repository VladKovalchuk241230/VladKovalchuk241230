class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __len__(self):
        return self.x * self.y


class Point3D:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __len__(self):
        return self.x * self.y * self.z

    def __bool__(self):
        return self.x == self.y == self.z

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def __getitem__(self, item):
        if 0 <= item <= len(self.marks):
            return self.marks[item]
        else:
            return 0
    def __setitem__(self, key, value):
        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None] * off)
        self.marks[key] = value

    def __delitem__(self, key):
        del self.marks[key]

class StudentBreda:
    def __init__(self,name,marks,hello_array):
        self.name = name
        self.marks = marks
        self.hello_array = hello_array
    def __getitem__(self, item):
        if 0 <= item <= len(self.marks):# you can test it by changing marks to hello_array
            return self.marks[item]
        else:
            return 0
class FloatIter:
    def __init__(self,start=0.0,stop=0.0,step=0.5):
        self.start = start
        self.stop = stop
        self.step = step
        self.value = self.start
    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration
    def __iter__(self):
        self.value = self.start - self.step
        return self

class FloatIter2D:
    def __init__(self,start=0.0,stop=0.0,step=0.5,rows=5):
        self.rows = rows
        self.iter = FloatIter(start,stop,step)
    def __iter__(self):
        self.value = 0
        return self
    def __next__(self):
        if self.value < self.rows:
            self.value += 1
            return iter(self.iter)
        else:
            raise StopIteration
class FloatIter2DImproved:
    def __init__(self,start=0.0,stop=0.0,step=0.5,rows=5):
        self.rows = rows
        self.current_row = 0
        self.start = start
        self.stop = stop
        self.step = step
        self.current_value = 0.0
    def __iter__(self):
        self.current_value = self.start - self.step
        self.current_row = 0
        return self #must return self
    def __next__(self):
        if self.current_value + self.step < self.stop:
            self.current_value += self.step
            return self.current_value
        elif self.current_row < self.rows - 1:
            self.current_row += 1
            self.current_value = self.start
            return self.current_value
        else:
            raise StopIteration
class Geom:
    name = 'Geom'
    def __init__(self,x,y):
        self.set_coords(x,y)
    def set_coords(self,x,y):
        self.x = x
        self.y = y
class Line(Geom):
    name = 'Line'
    pass
class Rect(Geom):
    pass
class Vector(list):
    def __str__(self):
        return '// //'.join(map(str,self))
class Goods:
    def __init__(self,name,weight,price):
        super().__init__() #calls next init based on mro (Goods, MixinLog) = next = MixinLog
        print("init goods")
        self.name = name
        self.weight = weight
        self.price = price
    def print_info(self):
        print(f'info - {self.__dict__}')
class MixinLog:
    ID = 0
    def __init__(self):
        print("init MixinLog")
        MixinLog.ID += 1
        self.id = MixinLog.ID
    def save_sell_log(self):
        print(f'{self.id} sold !')
    def print_info(self):
        print(f'info from mixinlog')
class NoteBook(Goods,MixinLog):

    def print_info(self):
        MixinLog.print_info(self)#second solution
    pass

class Limited:
    __slots__ = ('x','y')#sets allowed local  properties
    #doesnt limit class attributes

    #decreases memory usage
    # makes work with local properties faster
    # limit on creating local properties
    my_name = 'vlad'
class Limited2D(Limited):
    __slots__ = () #x,y only
def test_1():
    point = Point(2,42)
    print(f'len - {len(point)} for Point(2,42)   bool - {bool(point)} if len == 0 bool equal false otherwise true')
    point = Point(0,0)
    print(f'len - {len(point)} for Point(0,0) bool - {bool(point)} if len == 0 bool equal false otherwise true')
    point = Point3D(2,3,4)
    print('Point3D(2,3,4) - ',bool(point), ' now magic bool func added,  bool not connected to len anymore ')
    point = Point3D(2, 2, 2)
    print('Point3D(2,2,2) - ', bool(point),' now magic bool func added,  bool not connected to len anymore ')
    #can be used like : if point:
def test_2():
    student = Student('Vlad',[20,20,10,10,15,10,15])
    print('student[2] = ',student[2]) #__getitem__
    print('student[20000] = ', student[20000])  # __getitem__
    student[2] = 2
    print('student[2] = 2 / student[2] =  ', student[2])  # __getitem__
    student[12] = 12
    print('student[12] = 12 / student =  ', list(student))  # __getitem__
    new_student = StudentBreda('vlod',[2,3,4,5,5],[0,0,0,0,-1])
    print(list(new_student),'StudentBreda __getitem__ makes it possible to get list from class')
    print(tuple(new_student), 'StudentBreda __getitem__ makes it possible to get tuple from class')
    del student[12]
    print('del student[12] = ',list(student))
def test_3():
    iterator = iter(range(0,7,2)) #0,2,4,6
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print("next texts float iter (0,6)")
    for n in FloatIter(0,6):
        print(n)

    print("next texts float iter 2D (0,6)")
    for row in FloatIter2D(0,6,0.5,3):
        for x in row:
            print(x, end = " ")
        print()
        print("next texts float iter 2D Improved (0,6)")
    for value in FloatIter2DImproved(0,6,0.5,3):
        print(value, end = " ")
        #print()
    print()
def test_4():
    rect = Rect(2,132)
    #rect.set_coords(2,5)
    print(rect.__dict__)
    line = Line(1,33)
    print(f'line name - {line.name} and rect name - {rect.name}')
    print(line.__dict__)
    print('Line issubclass Geom',issubclass(Line,Geom))
    print('line issubclass Geom', issubclass(line.__class__, Geom))
    print('line isinstance Geom', isinstance(line, Geom))
    print('line isinstance Line', isinstance(line, Line))
    v = Vector([12,3,5,6,6,3,1,23,2])
    print(v)
def test_5():
    mine_notebook = NoteBook('my',1111,40000)
    print(mine_notebook.__dict__)
    mine_notebook = NoteBook('my', 234, 23)
    print(mine_notebook.__dict__)
    mine_notebook = NoteBook('my', 1333, 4242)
    print(mine_notebook.__dict__)
    mine_notebook.print_info() # calls Goods(now no because i defined print_info in Notebook class) as it first in mro, but i want to call it from MixinLog we have 2 options check them above and in norebook class
    MixinLog.print_info(mine_notebook) # solution
def test_6():
    limited = Limited()
    limited.x = 10
    print(limited.my_name)
    limited = Limited2D()
    limited.x = 20
    print(limited.x)
def test_7():
    val1 = 5
    val2 = 1
    try:
        test_value = 'shared with exept else and finally?'
        val1 /= val2
        print('val1 /= val2 = ',val1)

    #except ZeroDivisionError as error:
      #  print("error - %s"%(error))

    except ArithmeticError as error:
        print("error - %s" % (error),test_value)
    else:
        print("no errors! works only if no exeptions ocurred",test_value)
    finally:
        print("finally execured! works in both cases",test_value)#executes before return! if we have return
def main():
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    test_6()
    test_7()
if __name__ == '__main__':
    main()
    pass
