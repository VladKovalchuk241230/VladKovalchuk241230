import math
import math as VladMath
import random
import statistics
import this
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
name = 'Vlad'
def functions_exercise3dot1():
    print(f'largest character = {max(name)}, smallest character = {min(name)}')
    print(f'testing max value in list - {max([1,2,3,4,5,6,24,1,2,4])}')
def functions_exercise3dot2():
    print(f'My name length - {len(name)}\nList size - {len([2,1,3,4,5,6])}')
def functions_exercise3dot3():
    print(f'My name type{type(name)}')
    print('min,max,len used above')
    calculate_x,calculcate_y = '5','5'
    print(f'convert string(x={calculate_x},y={calculcate_y}) to int and add them = {int(calculate_x)+int(calculcate_y)}')
    my_age = 180
    for index in range(len(str(my_age))):
        print(f'My age = {my_age}, at index {index} = {str(my_age)[index]}')
    infinitive_float = float('inf')
    print(f'infinitive float = {infinitive_float} type - {type(infinitive_float)}')
def functions_exercise3dot4():
    print(f'math module factorial for 4 = {math.factorial(4)}')
def functions_exercise3dot5():
    print(f'random uniform(1,4) = {random.uniform(1,4)}')
    print(f'choose random element from list = {random.choice([1,2,3,4,5,6,7,2,2,132,1,42,42,])}')
def functions_exercise3dot7():
    list3dot7 = [0.5, 2.1, 2.8]
    print(f'standart devitation for {list3dot7} = {statistics.stdev(list3dot7)}')
def functions_exercise3dot8():
    print(f'square root of 16 = {VladMath.sqrt(16)}')
def functions_exercise3dot9():
    #check console beggining
    pass
def print_hello():
    print("Hello!")

def functions_exercise3dot10():
    print_hello()
def print_name(name_to_print):
    print(name_to_print)
def functions_exercise3dot11():
    print_name(name)
def get_sum_from_two_arguments(x,y)->int:
    """
    calculate the sum of 2 argiments
    :param x: 1(int) argument to add
    :param y: 2(int) argument to add
    :return: (int) 1+2 argument
    """

    return x+y
def functions_exercise3dot12():
    print(f'sum of 5 and 10 is {sum([5,10])}')
    print(f'sum of 5 and 10 is {get_sum_from_two_arguments(5,10)}')
def functions_mutable_lists_check():
    list_a = [1,2,3,4]
    list_b = list_a #list_b makes reference to the same value as list_a
    list_b.append(1)
    print(list_a) #after changing list_b, list_a also changed because they both reference to same value

    list_c = [1,2,3,4]
    list_d = list_c + [1,1] #now list_d is new list in memory, since we concetanted 2 arrays
    print(list_d)
class student:
    def __init__(self,name,age,grade):
        self.name,self.age,self.grade = name,age,grade
    def get_grade(self):
        return self.grade
class course:
    def __init__(self,name:'BaseCourse',max_students:2):
        self.name = name
        self.max_students = max_students
        self.students = []
    def add_new_student(self,student:student)->bool:
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    def get_average_grade(self) -> float:
        return sum([student.get_grade() for student in self.students ])/len(self.students)
class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show_info(self):
        print(f'I am {self.name} and my age - {self.age}')
    def speak(self):
        print("I dont know what to say")
class Dog(Pet):
    def speak(self):
        print("Gawk")
        #self.speak()
class Cat(Pet):
    def speak(self):
        print("Mewk")
class Fish(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("blob")
    def show_info(self):
        print(f'I am {self.name} and my age - {self.age} and my color - {self.color}')
class Person:
    number_of_people = 0
    def __init__(self,name):
        self.name = name
        Person.add_person()
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1
    @classmethod
    def get_number_of_people(cls):
        return cls.number_of_people
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b


def computepay(hours, rate):
    """
    Compute the weekly pay of an employee.

    Parameters:
    hours (float): The number of hours worked in a week.
    rate (float): The hourly rate of pay.

    Returns:
    float: The total weekly pay. if employee worked 40 hours, each next hour rated x1.5.
    """
    if hours > 40:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * (rate * 1.5)
        total_pay = (40 * rate) + overtime_pay
    else:
        total_pay = hours * rate

    return total_pay


def convert_temperature(temperature, unit):
    """
    Convert temperature between Celsius and Fahrenheit.

    Parameters:
    temperature (float): The temperature value to be converted.
    unit (str): The unit of the temperature ('C' for Celsius, 'F' for Fahrenheit)

    Returns:
    float: The converted temperature in the opposite unit.
    """

    if unit == 'C':
        return (temperature * 9 / 5) + 32
    elif unit == 'F':
        return (temperature - 32) * 5 / 9
    else:
        raise ValueError("Invalid unit. Use 'C' for Celsius or 'F' for Fahrenheit")
def loops_exercise4dot1():
    total = 0
    num_to_add = 1
    while num_to_add <= 5:
        total += num_to_add
        num_to_add += 1
    print(f'total - {total} num_to_add - {num_to_add}')
    pass
def loops_exercise4dot2():
    n = 5
    while n > 0:
        print(n)
        n = n - 2 #skip
    print('Blastoff!')
def loops_exercise4dot3():
    to_square = [3, 0, 10, -5]
    [print(value**2) for value in to_square]#
def loops_exercise4dot4():
    count = 0
    for itervar in [3, 41, 12, 9, 74, 15]:
        count += itervar # +1 if it must be list len
    print('Count:len ', len([3, 41, 12, 9, 74, 15]))
    print('Count: ', count)
    print(f'Count: {sum([3, 41, 12, 9, 74, 15])}')
def loops_exercise4dot5():
    # Modify this loop such that it finds the sum of odd numbers in the list.
    # Expected answer is 68
    total = 0
    for itervar in [3, 41, 12, 9, 74, 15]:
        if itervar % 2 != 0:
            total = total + itervar
    print('Total: ', total)
def loops_exercise4dot6(values):
    smallest = None
    for val in values:
        if smallest is None or val < smallest:
            smallest = val
    return smallest
def loops_exercise4dot7(values):
    return len([val for val in values if val < 0])
def loops_exercise4dot8():
    for n in range(1,7):
        for a in range(1,7):
            print(a,n)
def loops_exercise4dot9(values):
    return len([val for val in values if val < 0]) != 0
def loops_exercise4dot10(values):
    values = values[:4]
    print(values)
    return len([val for val in values if val < 0]) != 0
def loops_exercise4dot11(value):
    sum_appeared :float = 0.0
    for n in range(1,7):
        for a in range(1,7):
            if value == n+a:
                sum_appeared += 1
    return round(sum_appeared / (6*6) * 100,2)
def main():
    random.random()
    functions_exercise3dot1()
    functions_exercise3dot2()
    functions_exercise3dot3()
    functions_exercise3dot4()
    functions_exercise3dot5()
    functions_exercise3dot7()
    functions_exercise3dot8()
    functions_exercise3dot9()
    functions_exercise3dot10()
    functions_exercise3dot11()
    functions_exercise3dot12()
    functions_mutable_lists_check()
    student1 = student('Vlad',18,80)
    student2 = student('Andrii',17,90)
    ai_course = course("AI2025",2)
    ai_course.add_new_student(student1)
    ai_course.add_new_student(student2)
    print(ai_course.get_average_grade())

    my_dog = Dog('Bob',900)
    my_cat = Cat('Timosha',1800)
    my_fish = Fish('Bubbles',39000,'blue')
    my_dog.speak()
    my_cat.speak()
    my_fish.speak()
    my_cat.show_info()
    my_fish.show_info()

    me_as_human = Person('Vlad')
    friend_as_human = Person('Andrii')
    print(me_as_human.get_number_of_people())
    print(friend_as_human.get_number_of_people())
    print(Person.get_number_of_people())

    print(f'my MathCalculation Class works without any instance - {MathOperations.add(1,24)}')

    print('My Name -',name," I love Cocacola",sep='|||||')
    print("Hello My name Vlad",end = "|")
    print("Hello thats same line!")

    my_friends = ['vlad','andri','alex','bogdan']
    length = map(len,my_friends)
    print(list(length))
    do_magic_with_friends = map(lambda x:x[::-1],my_friends)
    print(list(do_magic_with_friends))
    print(my_friends) #Original array not changed

    filtered_friends = filter(lambda x: len(x) > 4,my_friends)
    print(list(filtered_friends))

    list_of_values = [1,2,3,4,5,6,2,31,24,2,1,24,2,3,24,2,42,4,21,41,4,14,12,4,124,12,412,4,124,24,14,2,42,4,124,12,412,4,12]
    print(sum(list_of_values,start=-1000))
    print(sum(list_of_values, start=1000))

    people = [
        {'name':'vlad','age':18},
        {'name': 'alex', 'age': 17},
        {'name': 'andrii', 'age': 19}
    ]
    sorted_people = sorted(people,key=lambda dict:dict['age'],reverse=True)
    print(sorted_people)

    tasks = ['go to breda','eat something','study some time','go home','write worklog']
    for index,task in enumerate(tasks):
        print(f'task{index+1} - {task}')
    print(list(enumerate(tasks)))
    #number_of_people shared between all class objects
    # Use a breakpoint in the code line below to debug your script.
    my_friends_names = ['vlad','andrii','alex','bodya']
    my_friends_ages = [18,17,19,200,2]
    combined_data_about_friends = list(zip(my_friends_names,my_friends_ages)) #zip
    print(combined_data_about_friends)

    file = open('test.txt','w')
    file.write('hello i am vlad\ni am 18 yo')
    file.close()#avoid memory leaks

    with open('test.txt','w') as file:
        file.write("hey my name is vlad") # way better, cooler and closes file automaticaly

    print(help(computepay))
    print(computepay(45,20))
    print(convert_temperature(1312087989,'F'))
    loops_exercise4dot1()
    loops_exercise4dot2()
    loops_exercise4dot3()
    loops_exercise4dot4()
    loops_exercise4dot5()
    print('smallest - ',loops_exercise4dot6([1,2,4,21,24,2,3,324,-1]))
    print('negative values count - ',loops_exercise4dot7([1,2,42,1,23,4,5,6,3,1,-1,-4,-5]))
    print('negative values count - ', loops_exercise4dot7([-1, 5, 3, 0, -100, -7, 15]))
    loops_exercise4dot8()
    print(loops_exercise4dot9([1,2,3,4,5]))
    print(loops_exercise4dot9([1, 2, 3, 4, 5,-1]))
    print(loops_exercise4dot10([1, 2, 3, 4, 5]))
    print(loops_exercise4dot10([1, 2, 3, 4, 5, -1]))
    print(loops_exercise4dot10([-1, 2, 3, 4, 5, -1]))
    for dice_values in range(2,13):
        print(f'chance to meet value {dice_values} when throw 2 dices equeal to {loops_exercise4dot11(dice_values)}')
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
