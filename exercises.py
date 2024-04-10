# INPUT

'''
age = input('What is your age? ')
print('Hello, I am {} yo'.format(age))
'''


'''
# fruit = input('What fruit do you like? ')
# veg = input('What veg do you like? ')
# print('You like {} aand you like {}'.format(fruit, veg))
'''


'''
string = "3"
num_of_apples = int(string) + 5
print(num_of_apples)
'''

'''
purchased_apples = input('How many apples did you buy? ')
print(type(purchased_apples))
total_apples = int(purchased_apples) + 5
print(total_apples)
# type()
'''

# multiline comment
'''
This sorta works as multiline comment
'''

'''
friends = input("How many friends?")
pizzas = int(friends) * 0.5

print("You need {} pizzas for {} friends".format(pizzas, friends ))
'''

#DATE-TIME

'''
import datetime

x = datetime.datetime.now()
print(x)
'''

'''
import datetime
my_date = datetime.date(2020, 12, 31)
print(my_date.strftime("%d-%b-%Y"))
'''


# FOR LOOP

'''
for number in range(5):
    print(number)
'''

'''
for character in "Banana":
    print(character)
'''

'''
for character in 'Banana':
    print('<' + character + '>')
'''

'''
for name in ['Mary', 'Ranjit', 'Fatima']:
    print(name)
'''

'''
for number in range(5):  # 0,1,2,3,4
    print("executing FOR LOOP - run No {}".format(number + 1))
'''

'''
total = 0
print("*** This statement is OUTSIDE THE LOOP")
print("Before the loop executes, our TOTAL is equal to = ", total, '\n')
print("--------------------------------------------------------")

for number in range(3):  # remember --> 0, 1, 2
    print("This is loop execution for digit: " + str(number) + " inside the loop \n")
print("Updating total... (+ 1) \n")

total = total + 1  # every time the loop executes, we add 1 to the total
print("--------------------------------------------------------")
print("***This statement We is OUTSIDE the loop now")
'''

# While Loop

''' 

# Example INFINITE 'while loop' that runs forever until the memory is 'blown'
store_capacity = 10
while store_capacity > 0:
    print('Please come in. Spaces available: ' + str(store_capacity))
    
# store_capacity = store_capacity - 1 ---> imagine that we forgot to add this logic!!!

print("\nPlease wait for someone to exit the store.")

'''

# FUNCTIONS

'''
# this is a function 
def hello():
    print("Hello, class!")

# and now we are calling it!
# hello()
'''

'''
# NOT: fonksiyon yazarken tab ile (indentation deniyor galiba buna) print ya da artık fonksiyon içinde ne varsa onu
# ileriye atmamiz gerekiyor. Yoksa hata mesaji aliyoruz!!!
def hello(name):
    print('Hello,', name)


hello('Maria')
hello('Kim')
hello('Olya')
'''

# Pass multiple arguments

''' 
def some_function(name, job):
	print(name, 'is a', job)


some_function('developer', 'Fiona')

'''

'''
def some_function(name, job='developer'):
    print(name, 'is a', job)


some_function('Fiona')
some_function('Fiona', 'manager')

'''

# RETURN VALUE

# Using return statement

''' 
def sum(x, y):
    return x + y


result = sum(10, 15)
print("result is: {}".format(result))
'''

# IMPORTANT NOTE !! Thhe result is none for thhe function below, because it's not returned!
'''
def sum(x, y):
    x + y


result = sum(10, 15)
print("result is: {}".format(result))
'''

'''
def circle_area(radius): #  add the radius argument inside the brackets
    area = 3.14 * (radius ** 2)
    return area
# add return statement


circle_1 = circle_area(10)
print(circle_1)
'''

''' 

def days_in_hours(days): 
    hours = days * 24
    return hours


print(days_in_hours(10))
'''


# FOR loop and FUNCTION

def times_two(num):
    result = num * 2
    return result


for number in range(3):  # 0,1,2
    calc_res = times_two(number)
print(calc_res)

