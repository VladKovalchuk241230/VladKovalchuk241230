import keyword
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def func_to_compare_both_arguments(arg1,arg2)->None:
    print(arg1 == arg2)
    pass
def bool_return_test():
    print(5>6, " 5>6")
    print(1 > 0, " 1>0")
    x : int = 11
    print(x >= 10 and x <= 12, "x >= 10 and x <= 12, x = %s"%(x))
def exercise2dot3():
    gold = 100
    gold -= 10
    # or
    if gold >= 100:
        print("you have enough gold to buy new weapon")
    else:
        print("you don't have enough gold to buy new weapon")
    #or
    print("you have enough gold to buy new weapon" if gold >= 100 else "you don't have enough gold to buy new weapon")
    #or
    print("you %s gold to buy new weapon"%("have enough" if gold >= 100 else "don't have enough"))



def exercise2dot7and8():
    number = 30

    if number % 2 == 0:
        if number % 3 == 0:
            if number % 5 == 0:
                print('Yes!')
    if number % 2 == 0 and number % 3 == 0 and number % 5 == 0:
        print('Yes!')

def calculate_salary(hours:float,money_per_hour:float) -> str:
    overtime_hours_needed = 40
    overtime_hours_x = 1.5
    salary = 0
    if hours >= overtime_hours_needed:
        worked_hours_with_above = hours-overtime_hours_needed
        salary += (worked_hours_with_above)*(money_per_hour*overtime_hours_x)
        hours -= (worked_hours_with_above)
    salary += hours * money_per_hour
    return f'salary - {salary}'
#or
def calculate_salary_second(hours: float, money_per_hour: float) -> str:
    overtime_hours_needed = 40
    overtime_hours_x = 1.5

    if hours > overtime_hours_needed:
        regular_hours = overtime_hours_needed
        overtime_hours = hours - overtime_hours_needed
        salary = (regular_hours * money_per_hour) + (overtime_hours * money_per_hour * overtime_hours_x)
    else:
        salary = hours * money_per_hour

    return f'salary - {salary}, for {hours} hours with rate {money_per_hour}/hrs'
def exercise2and11(score:float)->str:

    if score < 0.0 or score > 1.0:
        return "Error occupied with your grade!!!"
    table = {0.9:"A",0.8:"B",0.7:"C",0.6:"D",0.0:"F"}
    for point in table:
        if score >= point:
            return table[point]
def main1and2exercise(test_argument:int)->None:
    print("test argument - ",test_argument)
    print(f"test argument - {test_argument}")
    print("test argument - %s,  - %s"%(test_argument, "even more"))
    func_to_compare_both_arguments(1,"test comparison")
    for n in range(0, 36, 3):
        print(f' index{n}')
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
        print(arr[n:n + 3])

    for i in range(0, 36, 5):
        print(keyword.kwlist[i:i + 5])
    calculate_lightspeed()
    print(repr("test"))
    print(str("test"))
    quotient = 16 // 2
    print(quotient)
    print(1452 % 11)

    minute = 45
    percentage = minute / 60 * 100
    print('percentage - ', percentage)
    bool_return_test()
    exercise2dot3()
    x = 129
    print('x is even' if x % 2 == 0 else 'x is odd')
    PlayerID = 1
    if PlayerID == 0:
        print("player admin")
    elif PlayerID == 1:
        print("player superadmin")
    elif PlayerID == 2:
        print("player superadmin with cheats")
    else:
        print("player just a player")
    text_to_print = ""
    match PlayerID:
        case 0:
            text_to_print = "player admin"
        case 1:
            text_to_print = "player superadmin"
        case 2:
            text_to_print = "player superadmin with cheats"
        case _:
            text_to_print = "player just a player"
    print(text_to_print)
    exercise2dot7and8()
    first_add_value = 5
    second_add_value = "bad value"
    second_add_value_test = "bad value"
    try:

        #print(f'result {first_add_value + second_add_value}')
        print(f'result {first_add_value + second_add_value_test}')
    except:
        print('something went wrong, please check your variables!')

    num1 = 5
    num2 = 0

    try:
        ratio = num1 / num2
        print(f'ratio - {ratio}')
    except:
        print('trying divide by zero ? %s/%s'%(num1,num2))
    print(calculate_salary(30,20))
    print(calculate_salary_second(45,20))
    print(exercise2and11(0.8))
    print(exercise2and11(0.799999))
def calculate_lightspeed()->None:
    d = 1.5e8  # Earth - Sun distance in km
    v = 3e5  # speed of light in km/s
    seconds_result = d/v
    print(f'time needed - {seconds_result/60} mins ')
def main3exercise():
    my_name = "Vlad Kovalchuk"
    print("**EXERCISE 3 PART - FUNCTIONS**")

    print(type(32))
    print(type([1,2,3,4]))
    print(type({"name":"vlad","password":"qwertyui"}))
    string = "hello world!"
    # exercise 3.1

    print(f'max - {repr(max(my_name))} and min - {repr(min(my_name))}')

    # end
    list = [1,2,3,4,5,6,7,8,600]
    string_list = ['vlad kovalchuk','andrii bolschoymalchik','alex molodecbratancik']
    print(f'max - {repr(max(string))} and min - {repr(min(string))}')
    print(f'max - {repr(max(list))} and min - {repr(min(list))}')
    print(f'max - {repr(max(string_list))} and min - {repr(min(string_list))}')
    print(f'zero index - {repr(string_list[0])} and last index - {repr(string_list[-1])}')
    print(f'zero index - {repr(string_list[0])} and last index - {repr(string_list[len(string_list)-1])}')# -1 of len because indexes starts from 0

    # exercise 3.2

    print(f'My Name Length - {len("Vlad Kovalchuk")}')
    print(f'My Name Length - {len(my_name) - my_name.count(" ")}') #My name size without empty spaces

    # end

    # exercise 3.3

    print(type(32))
    print(type([1, 2, 3, 4]))
    print(type({"name": "vlad", "password": "qwertyui"}))
    print(f'max - {repr(max(string))} and min - {repr(min(string))}')
    print(f'max - {repr(max(list))} and min - {repr(min(list))}')
    print(f'max - {repr(max(string_list))} and min - {repr(min(string_list))}')
    print(f'zero index - {repr(string_list[0])} and last index - {repr(string_list[-1])}')
    print(
        f'zero index - {repr(string_list[0])} and last index - {repr(string_list[len(string_list) - 1])}')  # -1 of len because indexes starts from 0
    print(len("VERY VERY SHORT STRING"))
    num1, num2 = 5, "VladKovalchuk222"

    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        print("One of the values cannot be converted to an integer.")
    else:
        print(f'num1 + num2 = {num1 + num2}')

    # end



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main1and2exercise(1)
    main3exercise()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
