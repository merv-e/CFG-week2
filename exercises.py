# age = input('What is your age? ')
# print('Hello, I am {} yo'.format(age))


# fruit = input('What fruit do you like? ')
# veg = input('What veg do you like? ')
# print('You like {} aand you like {}'.format(fruit, veg))

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

''''''
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
