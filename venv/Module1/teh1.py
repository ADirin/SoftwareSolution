import math
import random

# print('-------MODULE1--------------------------------MODULE1-------------------------')
# print('----------Teh1---------------------------')
# name = input('what is your name: ')
# print(' Hello: '+name)
# print('--------------Teh2-----------------------')
# sade = float(input('Give the radius: '))
# radus = float(sade * math.pi)
# print('the circle area is : ', radus)
# print('******************Teh3****************************')
# base = float (input('Enater the base: '))
# height= float(input('Enter the height: '))
# piiri = 2 * (base + height)
# pinta = base*height
# print('Here is the piiri', f"{piiri:.2f}")
# print('here is the area: ', f"{pinta:.2f}")
#
# print('******************Teh4****************************')
#
# num1 = float(input('enter the first number: '))
# num2 = float(input('enter the second number: '))
# num3 = float(input('enter the third number: '))
#
# sum = float (num1+num2+num3)
# avg= float (sum / 3)
# print('here is the sum: ', sum)
# print('here is avg: ', avg)
#
# print('+++++++++++++Alternative Solution+++++')
# summa =0
# avgs =0
#
# for i in range (3):
#     number = float(input("Enater numbe {}: ".format(i+1)))
#     summa += number
# avgs= summa /3
# print ('here is sum ', summa)
# print('here is the AVG: ', avgs)

# print('------------------------Teh5----------------------------')
#
# talent = float (input('give talents: '))
# pounds = float(input('give pounds: '))
# lots = float(input('give lots: '))
# total  = float((talent * 20) + (pounds*32) + lots)
# kilo = float (total * 13.3) //1000
# gram =float (total*13.3) % 1000
# print ("The weight in modern units: ".kilo, ' kilograms and ', gram, ' grams.'   )

# print('------------------------Teh6----------------------------')
# code3 = ""
# code3 = str(random.randint(0,9))+ str(random.randint(0,9)) + str(random.randint(0,9))
# code4=""
# code4 = str(random.randint(1,6))+ str(random.randint(1,6)) + str(random.randint(1,6))+ str(random.randint(1,6))
#
# print('the code 3: ', code3)
# print('the code 3: ', code4)
#
# print('+++++++++++++Alternative Solution+++++')
# code3 = ""
# for i in range(3):
#     num1= random.randint(0,9)
#     code3 +=str(num1)
#
# code4 = ""
# for i in range(4):
#     num2 = random.randint(1,6)
#     code4 += str(num2)
# print('the numbers: ', code3)
# print('the numbers: ', code4)
print('---------------------------Conditional Structure (if)-----------------------------------------')
# print('------------------------3_Teh1----------------------------')
# size = float(input("entere the fish size "))
# if size >= 42:
#     print('good catch ', size)
# else:
#     print("does not meet", size, " the length realse it ")
#
print('------------------------3_Teh2----------------------------')
#
# cabinClass = ""
# cabinClass = str(input('Enter the cabin class: '))
# if (cabinClass ==  "LUX"):
#     print("Upper Deck cabin with a balcony")
# elif cabinClass== "A":
#     print("Above the car with windo")
# elif cabinClass == "B":
#     print("Above the car")
# elif cabinClass == "c":
#     print("Above the below car deck")
# else:
#     print("Invalid cabin class")

# print('------------------------3_Teh3----------------------------')
# gen = ""
# hemo=0.0
# gen = str (input('Are you male or female: '))
# hemo = int (input(' Enter the hemo value: '))
# if ((gen == "female") & ( 117<=  hemo <= 155 )):
#     print ('for female', hemo,  ' is Normal  ')
#
# if ((gen == "male") & (134<=hemo <= 167 )):
#      print ("for male", hemo, " is Normal value ")
# elif (gen ==""):
#     print("wrong input")

# print('------------------------3_Teh4----------------------------')
#
# year = 0
#
# year = int(input('Enter the year '))
# if  ((year % 4 == 0 and  year % 100 != 0) or (year % 400 ==0)):
#     print( year,' is a year')
# else:
#     pass

print('-------------------------While Loops (while)---------------------')
# print('-------------------4_teh1-------------------')
# i = 1
# while (i < 1000):
#     if (i % 3 ==0):
#         print(" the divisible value is: ", i)
#     i +=1
# print('-------------------4_teh2-------------------')
# i = 0.0
# i = float (input("enter the value in inches"))
# while (i >0):
#     cen = i * 2.54
#     print( i, " in inches is equal", cen, " centimeter")
#     i = float (input("enter the value in inches"))
# print("bye ")

print('-------------------4_teh3-------------------')

#
# smallest = None
# largest = None
# while True:
#
#     ans = input("Enter a number or Enter quite")
#     if ans == "":
#         break
#     try:
#         num = int(input("Enter the number: "))
#         if smallest is None or num < smallest:
#             smallest= num
#         if largest is None or num > largest:
#             largest = num
#     except ValueError:
#         print("Invalid input: ")
# if smallest is not None and largest is not None:
#     print('smallest: ',  smallest)
#     print('largest: ', largest)
#
# else:
#     print('No Number ')

# print('-------------------4_teh4-------------------')
# x = random.randint(1,10)
# print(x)
# while True:
#     num = int(input('guess a number: '))
#     if x ==num:
#         break
#     elif x >= num:
#         print('your number is too small')
#     else:
#         print('your name is too high')

# print('-------------------4_teh5-------------------')
# USERNAME = "amirDirin"
# PASSWD= "1234"
#
# login = str(input('enter user name: '))
# passw = str(input('enter passwd; '))
# counter = 0
# while True:
#     if (login == USERNAME and passw == PASSWD):
#         print('welcome')
#         break
#
#     else:
#         login = str(input('enter user name: '))
#         passw = str(input('enter passwd; '))
#     counter = counter+1
#     print('Your tried:  ', counter, '/5 ')
#     if login != USERNAME and passw != PASSWD and counter == 5:
#         print('Access Denied, you have already ', counter, ' times tried')
#         break
#
print('-------------------4_teh6****!!!!!-------------------')
# chatGPT solution
import random

num_points = int(input("Enter the number of random points to generate: "))
points = [(random.uniform(-1, 1), random.uniform(-1, 1)) for _ in range(num_points)]
points_inside_circle = sum(1 for x, y in points if x**2 + y**2 < 1)

pi_approximation = 4 * points_inside_circle / num_points
print("Approximation of pi:", pi_approximation)