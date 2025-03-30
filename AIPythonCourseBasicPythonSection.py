# Variables and constants
# adding a new commint from Git Hub

# input an number and use int to make sure its an integer.  if we don't use int it will be a string and will print with single quotes around it
age = int(input('type your age: '))
print('Your age is', age)

a = 1
b = 2
c = 3
d = 'coffee'
print(' I have {} and {} and {} tacos and {} babio'.format(a, b, c, d))

# Mathmatical operations
number1 = -3
number2 = 14
number3 = 15

print(number2)
print(number1,number3)
float1 = 3.14
float2 = 2.71
print(float1,float2)
letter = 'a'
word1 = 'programming language'
word2 = 'python'
print(letter,word1,word2)
print('this',word1, 'is called',word2)

a = 5
b = 3
print(a,b)
print('the sum is', a + b)

print('The subtraction is', a - b)

# input an number and use int to make sure its an integer.  if we don't use int it will be a string and will print with single quotes around it
age = int(input('type your age: '))
print('Your age is', age)

speed = float(input('Type the speed: '))
print('The speed is', speed)

name = str(input('What is your name?'))
print('Your name is',name)

# the .2f below is saying only show 2 decimal places in the float number
txt = "I have {an:.2f} Rupees!"
print(txt.format(an = 4))


a = 5
b = 3
a + b
print('The sum is', a + b)
print('The subtraction is', a - b)
print('The multiplication is', a * b)
print('The division is', a / b)
# use % to get the "rest" or REMAINDER of the division meaning 3 * 3 is 9 and 10 - 9 is one so you get one
# you can us this to test if the remainder is odd or even.  Even will result in zero, odd will result in a 1
print('The rest is', 10 % 3)

# exponents using double star **
print('5 to the power of 4 is',5**4)
# same as this:
5 * 5 * 5 * 5

# now let's import the math library
import math
math.sqrt(81)

a = 5
b = 3
print('The division is', round(a / b, 4))
print('The division is', round(a / b, 1))

# STRINGS
a = 'python'
print(a)
upper = a.upper()
print(upper)
lower = a.lower()
print(lower)
capital = a.capitalize()
print(capital)
# we will access the specific indexes of a string below.  Note index 0 is the first character of the string
# when we use a range, the last character in the range is not returned.  So below will only print a throuhg 2 and not show what's in index 3
middle = a[0:3]
print(middle)
# shows end of the string from index position 3 to the end
last = a[3:]
print(last)
# replace a character in a string
b = a.replace('y', 'i')
print(b)
# replace multile characters in the string
c = a.replace('th', 'ht')
print(c)
# find will search for a letter and return the index position.  h is in postion 2 so that will be returned
c.find('h')
# if we use find and the letter is not present in the string, it will return -1
c.find('m')
# length
len(c)
d = ' python '
print(len(d))
# remove spaces
e = d.strip()
print(len(e))

# to print a single quote as part of a string, you can use double quotes
a = True
b = False
c = a & b
print("Are 'A' and 'B' equal?",c)

n1 = 14
n2 = 16
print('n1 dievided by n2 is n1 / n2')
# if we just put them in brackets, not change
print('{n1} dievided by {n2} is n1 / n2')


# F-STRINGS and .format to add variables to print statements
# but if we add the letter "f" in front of the brackets, it becomes an "f-string" and we can pass it values
print(f'{n1} divided by {n2} is {n1 / n2}')

txt = "I have ${an:.5f} dollars!"
print(txt.format(an = 4))
# Output
# I have 4.00 Rupees!

# another .format example.  It just adds in the variables in sequence
a = 1
b = 2
c = 3
d = 'coffee'
print(' I have {} and {} and {} tacos and {} babio'.format(a, b, c, d))

# excercise 1:
# read two integer numbers, execute and display results fo the following
# operations: addition, subtraction, multiplicaiton, and division

print('EXCERCISE 1')
Num1 = int(input('enter the first number '))
Num2 = int(input('inter a second number '))
print(Num1 + Num2)
print(Num1 - Num2)
print(Num1 * Num2)
print(Num1 / Num2)

# Excercise 2:
# calculate the amount of liters of fuel spent on a trip considering a car that
# consumes 12 km per liter.  to obtain the calc, the user must provide the time
# spent on the trip and the average seed during the trip.  it is possible to
# obtain the distnace traveled using thee following equation:
# DISTANCE = TIME * SPEED. Then you can calc the liters using the following
# equation: LITERS = DISTNACE / 12.  The program must present the values of
# the average speed, time spend on the trip, the distnace traveled, and the
# amount of liters used on the trip

TimeSpentDriving = float(input('How many hours where you driving? '))
AverageSpeed = float(input('What was your average speed in KM/hr? '))
Distance = TimeSpentDriving * AverageSpeed
Liters = Distance / 12
print('')
# see below I'm using "\" and an escape character so I can have a single quote in my string
print('First we\'ll print them on separate lines:')
print('- Average speed was', AverageSpeed, 'KM/hr')
print('- Hours spent driving were', TimeSpentDriving)
print('- KMs driven were', round(Distance,2))
print('- Liters of fuel used for your trip were', round(Liters, 3))
# with f-string
print('')
print('*** Low lets use f-string to make it one big sentence! ***')
print(f'Your drove for {TimeSpentDriving} hours at an average speed of {AverageSpeed} KM/hr so you drove {round(Distance, 2)} KMs and used {round(Liters, 3)} liters of fuel during your trip!')

# LOGICAL OPERATORS AND OR AND NOT
a = True
b = False
print(a, b)
# AND operator
a and b
print(a, b)
# this is the same as using the word and
print(a & b)
# to print a single quote as part of a string, you can use double quotes
c = a & b
print(c)
print("Are 'A' and 'B' equal?",c)

# OR operator
print('a or b is', a or b)
#this is the same as using or
print('a | b is', a | b)

# not
# variable a is True so not a is False
print('not a is should be False:', not a)
# variable b is False so not a is True
print('not b is should be True:', not b)

# RELATIONAL OPERATORS relate two or more numbers
print(5 > 3)
print(5 < 3)
print(5 < 5)
print(5 >= 5)
print('compare if numbers are equal: 5 == 5 is', 5 == 5)
print('compare if numbers are NOT equal: 5 != 5 is', 5 != 5)

# Conditional operators - if else, For, and Do while
# using the colon at the end of the first line indents when you hit enter.
# other languages would require backets or something else to make it clear all:
# code on the lines is in one function

# since below is true, it will print the second line
if 5 > 3:
  print('5 is greater than 3')

# since below is false, it will not print the second line
if 1 > 3:
  print('1 is greater than 3')

# since below is false, it will not print the second line
if 1 > 3:
  print('1 is greater than 3')
else:
  print('1 is not greater than 3')

if 5 > 5:
  print('5 is greater')
elif 5 < 5: # elif is the same as else if
  print('5 is less')
else:
  print('5 must be equal')

n = 3
if n == 4:
  print('n is equal to 4')
else:
  if n == 3:
    print('n is equal to 3')
  else:
    print('n is not equal to 4 and is not equal to 3')

# below if y is even, the first statement will print but if odd, the second one will print
x = 2
y = 4

# will be true if x > 1 and the remaining of y divided by 2 equals 0
if (x > 1) and (y % 2 == 0):
  print("'x' is greater than 1 and 'y' is even")
else:
  print('One or more conditions are False')

# 15.155 HOMEWORK

# Exercise 1
# Read a user's age and classify he/she into:
# Child - 0 to 12 years old
# Teen - 13 to 17
# Adult - 18 or over
# if a negative number is entered, an error message must be shown

age = float(input('Please enter your age: '))
if (age >= 0) and (age < 13):
  print('You are enjoying the youth of childhood!')
elif (age >= 13) and (age < 18):
  print('Cool, you\'re a teen, that\'s fire!')
elif (age >= 18) and (age <= 54):
  print('You\'re an adult and people look up to you!')
elif (age >= 55):
  print('Time is up, start settling your affairs old timer!  Before you go, what were dinosaurs like?')
else:
  print('Invalid age!')

# Exercise 2
# use the mean calc to get the avgerage of a student by
# reading the grades G1, G2, and G3.  After the average
# is calculated, print if the student is approved, has
# failed, or has taken the exam. If the average is the range
# of 0.0 to 4.0, the student has failed.  If the average
# is in the range from 4.1 to 6.0 the student has taken
# the exam.  Finally, if the average is greater than 6 the
# student has been approved.  If the student took the exam,
# the exam grade must be read.  If the exam grade is greater
# than 6.0, he/she is approved, otherwisek, is failed
G1 = float(input('Enter grade 1 is '))
G2 = float(input('Enter grade 2 is '))
G3 = float(input('Enter grade 3 is '))

dataSet1 = [G1, G2, G3]

import numpy as np
AvgGrade = round(np.mean(dataSet1), 2)
print(AvgGrade)

if (AvgGrade >= 0.0) and (AvgGrade <= 4.0):
  print('You have failed!')
elif (AvgGrade >= 4.1) and (AvgGrade <= 5.9):
  exam = float(input('Enter the exam grade here: '))
  if exam >= 6.0:
    print('You are approved, your exam saved you!')
  else:
    print('You have failed!')
elif (AvgGrade >= 6.0):
  exam = input('Enter the exam grade here: ')
  print(f'You are approved!  Your GPA is {AvgGrade} and your exam is {exam}')
else:
  print('Invalid data entered.')

#For Loop

# wrong way
print(1)
print(2)
print(3)
print(4)
print(5)

# right way
# note you need to have one higher than the highest number you want to print
# so we need to use 6, not 5, to get to 5
# for loop using numbers
for number in range(1,6):
  print(number)

for number in range(5, 0, -1):
  print('this time in reverse', number)

sum = 0
for number in range(1,6):
  print('number is', number)
  sum = sum + number
  print('sum is', sum)
print('sum is', sum)

# for loop using a string
word = 'python'
for letter in word:
  print(letter)
  if letter == 'h':
    print('It has found letter h')

# nested for loop
for i in range(0,5):
  print(i)
  print('------')
  for j in range(0,3):
    print(j)
  print()

# While loop
number = 1
while number < 6:
  print(number)
  # this is the traditional way to do it but below is sleeker:
  #number = number + 1
  number += 1

number = 5
while number > 0:
  print('before decrement', number)
  # this is the traditional way to do it but below is sleeker:
  #number = number + 1
  number -= 1
  print('number is decrementing', number)

# While loop
sum = 0
number = 1
while number < 6:
  print(number)
  # this is the traditional way to do it but below is sleeker:
  #number = number + 1
  sum += number
  number += 1
print('sum', sum)

# this is a way to use a while loop for data validation
grade = 13
while grade < 1 or grade > 10:
  grade = float(input('Type a grade from 0 to 10: '))


# 15.159 homework
# excercise 1
# Read 5 numbers and caclulate the average
# n = 3
number = average = sum = 0
for n in range(0,6):
  sum += n
  n += 1
print('sum', sum)
average = sum / 5
print('average', average)
n = 0
sum = 0
average = 0

# exercise #1 his way with a for loop:
number = average = sum = 0
print(number, average, sum)

# NOTE: the underscore can be used if we don't need the variable below so this will save some memory47

for _ in range(1, 6):
  number = float(input('Type the number'))
  sum += number
print(sum)

average = sum / 5
print('The average is', average)

# excercise #1 his way with while loop
number = average = sum = 0
sum = 0
number = 1
while number <= 5:
  score = float(input('Type the number/score:'))
  sum += score
  number += 1
print('The average is ', sum / 5)


# Excerise 2
# Print the multiplication from 1 to 30 considering number 3
# (3 x 1 = 3,...,3 x 10 = 30)
# using a while loop:
print('My way with while loop')
multp = 3
number = 1
while number < 11:
  product = number * multp
  print(f'{multp} x {number} = {product}')
  number += 1

# using a For loop.
print('My way with for loop')
multp = 3
number = 1
for num in range(0,10):
  product = number * multp
  print(f'{multp} x {number} = {product}')
  number += 1

# Exercise 2 his code for a for loop
for i in range(1,11):
  print('3 x {}  = {}'.format(i, 3 * i))

# exercise 3 his code for while loop
number = 1
while number <= 10:
  print('3 x {} = {}'.format(number, 3 * number))
  number += 1

txt = "I have ${an:.5f} dollars!"
print(txt.format(an = 4))
# Output
# I have 4.00 Rupees!

a = 1
b = 2
c = 3
d = 'coffee'
print(' I have {} and {} and {} tacos and {} babio'.format(a, b, c, d))


# COLLECTIONS

# Tuples - used (); can have duplicates
tuple1 = ('Dog', 'Cat', 'Horse', 'Horse')
# print all elements in tuple
print(tuple1)
# print element at index 0
print(tuple1[0])
# print the index number where 'Dog' is stored
print('index of dog in tuple is', tuple1.index('Dog'))
# use it in a for loop to print each element on a new line
for e in tuple1:
  print('tuple1', e)

# LISTS - uses []; can have duplicates
list1 = ['Cat', 'Dog', 'Horse']
list2 = ['Bird', 'Snake', 'Snake', 'Horse']
list3 = list1 + list2
print('list 3', list3)
list2_2 = list2 * 2
print('list2', list2_2)
list1[0], list1[1], list1[2]
print('printing each value in list', list1[0], list1[1], list1[2])
# access list by range.  note the 2 will be omitted and we'll get 0-1
print('print list1 by range', list1[0:2])
# append to list
print('list1 before append', list1)
list1.append('MondeyMan')
print('list1 after append', list1)
# remove from list
print('list1 before remove', list1)
list1.remove('Cat')
print('list1 after remove', list1)
# delete entire list
del(list1)
# print('list1 after delete', list1)

# use a for loop to print items in list
for item in list2_2:
  print('this is an item in list2_2:', item)

# DICTIONARY AND SET

# Dictionary - uses {}; must be unique key; unlike a tuple or
# list, you can store values for each of the "keys"

# below means there are 32 dogs, 22 cats, and 14 horses
animal = {'Dog': 32, 'Cat': 22, 'Horse': 14}
print(animal)
# if you want just the number of cats, you do this:
print('the number of cats is', animal['Cat'])

# add a key pair to the dictionary:
animal['Monkey'] = 99
print(animal)

# delete a key value pair:
del(animal)['Horse']
print(animal)

# see all pairs:
print(animal)
print(animal.items())

# see just keys
print(animal.keys())

# see just keys
print(animal.values())

#create new dictionary then add it to the first one
animal2 = {'Bird': 32, 'Snake': 22, 'Hippo': 14}
animal.update(animal2)
print('animal now updated with animal2', animal)

# now use for loop with dictionary to print the key and the value on same line
for a, v in animal.items():
  print('printing each pair in the dictionary', a,v)


# SETS

# create variable called set1, not yet defined as a set so when we
# print, we'll get all values including dups
set1 = ('A', 'B', 'C', 'D', 'B', 'C', 'C', 'C')
print(set1)
# defining it as a set will mean we get only the UNIQUE values
print(set(set1))

#let's create some sets then use INTERSECTION to show only the values
# in both sets:
s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7}
s3 = s1.intersection(s2)
print(s3)

# differences in sets
print(s1.difference(s2))
print(s2.difference(s3))

# MATRICES - ONE OF MOST USE STRUCTURES

import numpy
matrix = numpy.array([[2,3,1],
                     [4,5,6]])
print(matrix)

# check shape of matrix - returns 2 rows, 3 columns
print(matrix.shape)

# access  the first row
print(matrix[0])
print(matrix[1])
# access a single row and column - first row, second column
print(matrix[0][2])

# for loop with a matrix
for row in range(matrix.shape[0]):
  # print('row', row)
  print('matrix.row', matrix[row]) #this prints each rows separately
  for column in range(matrix.shape[1]):
    print('matrix row column', matrix[row][column]) # this prints each value one row at a time but shows them one line at a time

# HOMEWORK 15.164
# EXERCISE 1
# Implement a loop that reads 5 numbes and stores them in a list.  After
# reading, implement antoher loop to add all values
Total = 0
ages = []
for val in range(0,5):
  val = int(input('type your age: '))
  ages.append(val)
  # sum function on next line is not part of assignment but is the easier way!!!
  # Total = sum(ages)
  # if we don't set sum1 to zero here, it will bring in
  # last total each time and sum1 will be wrong / too high
sum1 = 0
for age in ages:
  sum1 += age
print(sum1)
print('the easier way to do this is to use sum function', Total)

# INSTRUCTORS SOLUTION
list_of_numbers = []
for _ in range(1, 6):
  number = int(input('Type the number: '))
  list_of_numbers.append(number)
  print(list_of_numbers)
  len(list_of_numbers)
  sum = 0
  for i in range(len(list_of_numbers)):
    sum += list_of_numbers[i]
  print('Sum is:', sum)



# HOMEWORK 15.164
# EXERCISE 2
# Implement a dictionary to store the name and grade of 3
# students (read the values using a loop structure).  Build a
# new loop to add all the grades and calculate the average
n = g = GPA = 0
NamesGrades = {}
for _ in range(0,3):
  n = (str(input('Please type your name: ')))
  g = (float(input('Please enter your grade: ')))
  NamesGrades[n] = g
  GPA += g
print(NamesGrades)
GPPPvg = GPA / 3
print(f'First way to limit decimals is here {GPPPvg:.4f}')
# print("%.2f" % GPAAvg)
GPA2 = 'The GPA is {:.2f}'.format(GPA / 3)
print('sencond way to format it', GPA2)


# INSTRUCTOR SOLUTION
students = {}
for _ in range(1, 4):
  name = input('Type the name of the student: ')
  grade = float(input('Type the grade: '))
  students[name] = grade
sum = 0
for grade in students.values():
  sum += grade
print('Average: ', sum / 3)


# HOMEWORK 14.164
# EXERCISE 3
import numpy as np
matrix = np.array([[3, 4, 1],
                  [3,1,5]])
Val = Val2 = 0
Num = 1
for row in range(matrix.shape[0]):
  # print('row', row)
  #print('matrix.row', matrix[row]) #this prints each rows separately
  for column in range(matrix.shape[1]):
    Val = (matrix[row][column])
    print(f'This is value of the # {Num} element in the matrix: {Val}')
    Val2 += Val
    Num = Num + 1
print('The sum of all values in the matrix is', Val2)


import numpy as np
matrix = np.array([[3, 4, 1],
                  [3,1,5]])
sum = 0
for i in range(matrix.shape[0]):
  for j in range(matrix.shape[1]):
    sum += matrix[i][j]
print('Sum: ', sum)

# functions are parts of code that are given an name and can be called multiple times
# advantages are reuse, modularity, and maintenance
# three types: 1) No parameters and no return, 2) Parameter but no return and
# 3) Parameter and return

# 1) no parameter, no return
def myFun():
  print('Hello from myFun')

# 2) pass in a parameter, nothing returned
def myFunParam(inText):
  print(inText)

def sum(a,b):
  print(a + b)

# 3) paramter and return
def sum1(a, b):
  print('Hello from sum1!!!')
  return a + b

# FUNCTIONS
myFun()
myFunParam('Sup playa')
sum(4,22)
sum1(45, 33)


r = sum1(5, 4)
print(r)

# setting c to 33 means if we don't pass a value to c, it will use 33 but if we
# do it will use what's passed
# let's use the three single quotes to document the goal of the funtion

def multiplier(a, b, c = 33):
  '''
  you can pass this funtions 2 or 3 numbers an it will multiply them
  '''
  return a * b * c

r = multiplier(11, 22)
print(r)
r2 = multiplier(11, 22, 9)
print(r2)
# either of the following will show us the comments iside of the three single
#quotes
multiplier()
help(multiplier)

# FUNCTIONS
"""
EXERCISE 1
Read a temperature in degrees Celsius and print it converted to degrees Fahrenheit.
The equation is , where F is the temperature in Fahrenheit and C
is the temperature in Celsius. Create the following functions:

Function to read and return the temperature value in degrees Celsius (no parameter)

Function to perform the calculation (receives as parameter the temperature in degrees Celsius)

Function to display the result (receives the result as parameter and only prints the result)
"""
def tempConverter(C):
  return (9 * C + 160) / 5
  # print(F)
  # return F

def printer(F):
  # print with two decimal place limit
  print(f'Your temp converted to Fahrenheit with only two decimals is: {F:.2f}')
  # print with no decimal place limit
  print('Your temp converted to Fahrenheit is: ', F)
def inputer():
  C = float(input('Enter a temp in Celsius to be conerted to Fahrenheit: '))
  F = tempConverter(C)
  printer(F)

inputer()

# EXERCISE 1 HIS SOLUTION
def read_temp():
  temp = float(input('type the temp in cels: '))
  return temp

def convert(temp_Cels):
  temp_f = (9 * temp_Cels + 160) / 5
  return temp_f

def show(temp_f):
  print('print converted to F: ', temp_f)

temp_c = read_temp()
temp_f = convert(temp_c)
show(temp_f)

"""
Exercise 2
Calculate the amount of liters of fuel spent on a trip considering a car that consumes
12 km per liter. To obtain the calculation, the user must provide the time spent on the
trip and the average speed during the trip. It is possible to obtain the distance traveled
using the following equation DISTANCE = TIME * SPEED. Then you can calculate the liters using
the following equation: LITERS = DISTANCE / 12. The program must present the values ​​of the
average speed, time spent in the trip, the distance traveled and the amount of liters used on the trip

Function to read the values (no parameter and returns both values inputted by the user)

Function to calculate the distance (receives time and speed as parameter and returns the distance)

Function to calculate the amount of liters (receives distance as parameter and returns the liters)

Function to display the result (receives all the values as a parameter and only prints the result)

"""

def inputer():
  time = float(input('How many hours where you driving? '))
  speed = float(input('What was your average speed in KM/hr? '))
  return time, speed

def calcD(time, speed):
  return time * speed

def calcL(distance):
  return distance / 12

def printer(time, speed, distance, liters):
  print('')
  # see below I'm using "\" and an escape character so I can have a single quote in my string
  print('First we\'ll print them on separate lines:')
  print('- Average speed was', speed, 'KM/hr')
  print('- Hours spent driving were', time)
  print('- KMs driven were', round(distance,2))
  print('- Liters of fuel used for your trip were', round(liters, 3))
  # with f-string
  print('')
  print('*** Low lets use f-string to make it one big sentence! ***')
  print(f'Your drove for {time} hours at an average speed of {speed} KM/hr so you drove {round(distance, 2)} KMs and used {round(liters, 3)} liters of fuel during your trip!')
  # with format
  print('')
  print('*** Low lets use .format to make it one big sentence again! ***')
  p = 'Your drove for {} hours at an average speed of {} KM/hr so you drove {:.3f} KMs and used {:.2f} liters of fuel during your trip!'.format(time, speed, distance, liters)
  print(p)

# setting two variables, t and s, equal to a function will pass those variables
# to the function.  in the inputer function, I'm returning time and speed,
# which will be assigned to t and s respectively.
t, s = inputer()
print('values returned from inputer() are: ', t, s)
d = calcD(t, s)
l = calcL(d)
printer(t, s, d, l)


# MATH MODULE and it's various functions
# see more at docs.python.org
import math as m
print(m.sqrt(9))

print(m.sin(45))

print(m.cos(45))
# log of 1000 with a base of 10
print(m.log(1000, 10))
# now without setting the base
print(m.log(1000))
# if you don't set the base, it will defaul to m.e which is 2.7182...
print(m.e)
print(m.log(32, 2))
print(m.log(9,3))

print(m.pi)

# RANDOM module - used to generate random numbers
# useful for checking probabilities
import random
print(random.random())
print(random.random())
print(random.random())
print(random.random())
print(random.random())

# generate random numbers in a range of 1 to 10
rr = random.randint(1, 15)
print(rr)

# similar to randint but you can specify, odd, even, or any number in the range
# random even numbers
print('random even numbers', random.randrange(0, 12, 2))
# any random number in the range
print('any random number in range', random.randrange(0, 12, 1))
# random odd numbers
print('random odd numbers in range', random.randrange(0, 12, 3))
# random but any numuber since no step was specified
# so I think this i the same as randint
print('random number but no step is specified', random.randrange(0, 12))

# let's create a list then randomly select an element from that list
x = ['K', 'd', 13, '34j', 'x']
print('randomly select an element from the list', random.choice(x))

# Import TIME module
import time as t
# this will be the current time in seconds
print(t.time())

#This block converts seconds to datetime format
from datetime import datetime
thisTime = t.time()
converted = datetime.fromtimestamp(thisTime).strftime("%A, %B %d, %Y %I:%M:%S")
print('This has been converted to GMT: ',converted)
print( ' ')

# use time to record process time
before = t.time()
l = []
for i in range(0, 100000):
  l.append(i)
after = t.time()

interval = after - before
print(f'Elasped time: {interval:.4f} seconds')

# using sleep for a delay
print(' ')
print('Finishing...')
t.sleep(2)
print('...')
t.sleep(2)
print('Good bye')

# DATETIME functions
import datetime as dt
# get current date
print(dt.date.today())
# get date and time.  note the values are coming from the Google collab
# servers so it may not be in my timezone
print(dt.datetime.now())
# set the date
date = dt.date(1970, 8, 12)
print(date)
print(date.day)
print(date.month)
print(date.year)

# set date and time
time = dt.datetime(1975, 8, 5, 12, 33, 15, 211125)
print(time)
# extract hour, minute, second
print(time.hour)
print(time.minute)
print(time.second)
# microsecond has 6 places.  if I set less than 6 numbers, it will add zeros
# in front of them.  So 321 becomes .000321 but 525252 will be .525252
print(time.microsecond)

# first step is to create two modules in some other IDE and save to my local
# drive.  I used VS Code to create CreateCustomModule.py with the "sum" and
# "multiply" functions in it.
# below I'm imorting the file so I can use the functions in it
import CreateCustomModule as cm

print(cm.sum(2, 3))

print(cm.multiply(2, 3, 2))

print(cm.div(10, 5))

# HOMEWORK 172
'''
Create a .py file with two functions

Function to read a string (receives a message as a parameter and returns what the user has typed)

Function to read a float number (receives a message as a parameter and returns what the user has typed)

Import the file in Google Colab and test the functions
'''

import Homework as hw

STRr = hw.readStr()

FLTr1 = hw.readFlt()

FLTr2 = hw.readFlt()

print('my string is:', STRr, ' my decimals are:', FLTr1, 'and', FLTr2)


# homework 173 instructor's solution
import read_messages as rm

text = rm.read_string('Type your name: ')
print(text)

car = rm.read_string('Type the model of your car: ')
print(car)

number1 = rm.read_float('Type a number: ')
print(number1)

number2 = rm.read_float('Type another number: ')
print(number2)
print(number1 + number2)


# Errors and exception
try:
  n = int(input('Type an integer number: '))
  print('If you are seeing this, you entered the right data type!  Here is what you typed: ', n)
except:
  print('Invalid number!')
else:
  print('And you can see this too becase you entered the right data type!')


# now add a while loop to the same code so it will keep asking until the entry is and integer:
while True:
  try:
    n = int(input('Type an integer number: '))
    print('If you are seeing this, you entered the right data type!  Here is what you typed: ', n)
  except:
    print('Invalid number!')
  else:
    print('And you can see this too becase you entered the right data type!')
    break

# now add a while loop to the same code so it will keep asking until the entry is and integer:
# buyt also define sections for specific types of errors
while True:
  try:
    n = int(input('Type an integer number: '))
    print('If you are seeing this, you entered the right data type!  Here is what you typed: ', n)
  except ValueError:
    print('Invalid number!')
  except KeyboardInterrupt:
    print('Interrupted by the user')
    break
  else:
    print('And you can see this too becase you entered the right data type!')
    break

# now add a while loop to the same code so it will keep asking until the entry is and integer:
# buyt also define sections for specific types of errors
while True:
  try:
    list1 = []
    val1 = float(input('Enter a decimal number: '))
    val2 = float(input('Enter another decimal number: '))
    list1.append(val1)
    list1.append(val2)
    div1 = list1[0] / list1[1]
    print(f'Decimal one diveded by decimal 2 is {div1:.3f}')

  except ValueError:
    print('Invalid decimal number!')
  except ZeroDivisionError:
    print('You can\'t have zero as a denominator!')
  except KeyboardInterrupt:
    print('Interrupted by the user')
    break
  else:
    print('Nice work, you entered the right data types!')
    break


# instructor's solution to homework 176
list_of_values = []
try:
  list_of_values.append(float(input('Type a number: ')))
  list_of_values.append(float(input('Type another number: ')))
  division = list_of_values[0] / list_of_values[1]
except ValueError:
  print('Invalid number!')
except ZeroDivisionError:
  print('You can\'t have zero as a denominator!')
# IndexError would only happen if we change the code and try divide by, for
# example value [0] by the wrong index like [2]
except IndexError:
  print('Invalid Index')
except KeyboardInterrupt:
  print('Interrupted by the user')
else:
  print(f'The division is {division:.2f}')
finally:
  print('End of program')


# reading and writing to text files
with open('/content/sentence.txt') as txt:
  for row in txt:
    print(row)

with open('/content/sentence.txt') as txt:
  r = txt.readlines()
  print('this is r:', r)

with open('txt2.txt', 'w') as txt:
  txt.write('hello everyone')

with open('/content/txt2.txt') as txt:
  for row in txt:
    print(row)

# homework 178
n = g = 0
NamesGrades = {}
for _ in range(0,3):
  n = (str(input('Please type your name: ')))
  g = (float(input('Please enter your grade: ')))
  NamesGrades[n] = g
  with open('namesGrades.txt', 'a') as txt:
    txt.write(f'{n},{g}\n')
with open('namesGrades.txt') as txt:
  for row in txt:
    print('printing row', row)

# instructurs code for HOMEWORK 178
students = {'Peter': 8.0, 'Maria': 10.0, 'John': 7.5}
students

with open('students.txt', 'w') as students_file:
  for students, grade in students.items():
    students_file.write(f'{students},{grade}\n')

with open('students.txt', 'r') as students_file:
  for row in students_file:
    print(row)


# The regular expression to detect an email address is
# \w+@\w+\.w+
'''
. - any character except new line
\d - digit
\D - not a digit
\w - word character (a-z, A-Z, 0-9, _)
\W - not a word character
\s - whitespace (space, tab, newline)
\S - not whitespace
^ - beginning of a string
$ - end of a string
? - zero or one occurence
"\" - used before metacharcters to specify their literal meaning
'''
# search will check the whole string
import re
sentence = 'Hello!  My phone number is (00)0000-0000'
print('We are using a regular expression to find the phone number', re.search(r'\(\d\d\)\d\d\d\d-\d\d\d\d', sentence))

import re
sentence = 'The license plate of my car is FRT-1988'
print('We are using a regular expression to find the license plate', re.search(r'[A-Z]{3}-\d{4}', sentence))

import re
email = 'My email address is test@testtr634fgsdfg.com'
print('We are using a regular expression to find the email address', re.search('\w+@\w+\.com', email))

# match will only search the begining of a string
import re
sentence = 'FRT-1988 is the license plate of my car'
print('We are using a regular expression to find a match for the license plate', re.match('[A-Za-z]{3}-\d{4}', sentence))

import re
sentence = 'My phone number is (00)0000-0000.  The old number was (11)1111-1111'
print('We are using a regular expression to find the phone number', re.findall(r'\(\d\d\)\d\d\d\d-\d\d\d\d', sentence))

import re
emails = '''Name: Test 1
email: test1@testtr634fgsdfg.com
Name: Test 2
email: test2@testtr634fgsdfg.com
Name: Test 3
email: test3@testtr63.com.br
'''
print('We are using a regular expression to find the email address', re.findall('\w+@\w+\.com', emails))

# HOMEWORK
import re
sentence = 'My house is on 78 Peter Street. The zipcode is 88388-000 and 11111-111. My website is https://www.iaexpert.academy/mystupidpath or http://iaexpert.com.br'
print(' ', re.findall(r'\d\d\d\d\d-\d\d\d', sentence))
print('instructor solution', re.findall(r'\d', sentence))
print(' ', re.findall(r' \d\d ', sentence))
print(' ', re.findall(r'\d{5}-\d{3}', sentence))
print(' ', re.findall(r'\w+:+//www.\w+\.com', sentence))
print(re.findall('https?://[A-Za-z0-9./]+',sentence))

class Triangle(object):
  def __init__(self,side1,side2,side3):
    self.side1 = side1
    self.side2 = side2
    self.side3 = side3

t1 = Triangle(5,3,2)
print(t1.side1, t1.side2, t1.side3)

t2 = Triangle(8,8,8)
print(t2.side1, t2.side2, t2.side3)

# create a new class and add base and height
class Triangle2(object):
  def __init__(self,side1,side2,side3, base, height):
    self.side1 = side1
    self.side2 = side2
    self.side3 = side3
    self.base = base
    self.height = height

  def area(self):
    return (self.base * self.height) / 2

  def perimeter(self):
    return self.side1 + self.side2 + self.side3

  def type(self):
    if self.side1 > self.side2 + self.side3:
      print('it is not a tringle')
    elif self.side1 == self.side2 or self.side1 == self.side3 or self.side1 == self.side3:
      print('isosceles triangle')
    else:
      return 'other type of triangle'

t1 = Triangle2(5,1,3,4,3)
print(t1.side1, t1.side2, t1.side3, t1.base, t1.height)
print('t1 area', t1.area())
print('t1 perimeter', t1.perimeter())
print('t1 type', t1.type())

t2 = Triangle2(8,8,8,7,7)
print(t2.side1, t2.side2, t2.side3, t2.base, t2.height)
print('t2.area', t2.area())
print('t2 permimeter', t2.area())
print('t2 type', t2.type())


# create a new class student and create the constructure (init)
grade1 = grade2 = GPA = avg1 = 0
class student():
  def __init__(self,name, grade1, grade2):
    self.name = name
    self.grade1 = grade1
    self.grade2 = grade2
    self.average = 0.0


  def average(self):
    return (self.grade1 + self.grade2) / 2

  def show(self):
    print('I\'m in show',self.name, self.grade1, self.grade2)

  def results(self):
    if (self.grade1 + self.grade2) / 2 > 6:
      print('you passed')
    else:
      return 'you failed'


s1 = student('Jill',7,6)
print(s1.name, s1.grade1, s1.grade2)
print('s1 average', s1.average())
print(s1.show())
print(s1.results())

s2 = student('Jack',5,5)
print(s2.name, s2.grade1, s2.grade2)
print('s2 average', s2.average())
print(s2.show())
print(s2.results())


# instructor solution:
class Student2:
  def __init__(self,name, grade1, grade2):
    self.name = name
    self.grade1 = grade1
    self.grade2 = grade2
    self.average = 0.0

  def calculate_average(self):
    self.average = (self.grade1 + self.grade2) / 2
    return self.average

  def show_data(self):
    print(f'Name: {self.name}')
    print(f'Grade 1: {self.grade1}')
    print(f'Grade 2: {self.grade2}')
    print(f'Average: {self.average}')

  def results(self):
    if self.average > 6:
      print('You passed!')
    else:
      print('You failed!')


student11 = Student2('Peter', 7, 7.7)
average = student11.calculate_average()
print(student11.name, student11.grade1, student11.grade2)
print(student11.calculate_average())
print(student11.show_data())
print(student11.results())

student22 = Student2('Jayne', 3, 7.7)
average = student22.calculate_average()
print(student22.name, student22.grade1, student22.grade2)
print(student22.calculate_average())
print(student22.show_data())
print(student22.results())
