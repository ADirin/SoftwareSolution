import math
import random
import array

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

#print('-------------------------While Loops (while)---------------------')
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

#print('-------------------4_teh3-------------------')

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
#print('-------------------4_teh6****!!!!!-------------------')
# # chatGPT solution
# import random
#
# num_points = int(input("Enter the number of random points to generate: "))
# points = [(random.uniform(-1, 1), random.uniform(-1, 1)) for _ in range(num_points)]
# points_inside_circle = sum(1 for x, y in points if x**2 + y**2 < 1)
#
# pi_approximation = 4 * points_inside_circle / num_points
# print("Approximation of pi:", pi_approximation)

# print('-------------------5_teh1------------------------')
# arpa= int(input("How many numer cubes you have: "))
# total = 0
# for _ in range(arpa):
#     num = random.randint(1,6)
#     print('the num', num)
#     total += num
#
# print('sum of the numbers ', total)

# print('-------------------5_teh2-----------------------')
# a =  []
#
# while True:
#     num = (input("Enter the number: "))
#     if num == "":
#         break
#     a.append(int(num))
#
#     a.sort(reverse = True)
#
# print('five largest:  ')
# for i in range(5):
#     if i < len(a):
#         print(a[i])
#     else:
#         break
# print('-------------------5_teh3-----------------------')
#
# num = []
# while True:
#     luku = int(input('Enter an integer number: '))
#     if  luku < 2:
#         print('emty entry or less then two')
#         break
#     else:
#         isPrime = True
#         for i in range (2, int (luku**0.5) +1):
#             if luku % i == 0:
#                 isPrime = False
#                 break
#         if isPrime:
#             num.append(luku)
#             print(luku, " is prime")
#         else:
#             print(luku, " is not prime")
#     for i in range (len(num)):
#         print('the prime list is ', (num[i]))
#
# print('-------------------5_teh4-----------------------')
# city = [5]
# for i in range(1,6):
#     kaup = str(input('enter the city name '))
#     city.append(str(kaup))
# #for i in range(6):
# print('here are the list: ', city)
# print('the third city: ', city[3])
# print('-------------------6_teh1-----------------------')
# num = []
# def randomValue():
#     luku = int(random.randint(1,6))
#     return luku
# def mainProg():
#     while True:
#         number = int(randomValue())
#         num.append(number)
#     # print('The number', number)
#         if number == 6:
#             print('Bingo, You got six ')
#             break
#     for i in range (len(num)):
#         print('the numbers ', num)
#         break
# mainProg()

# print('-------------------6_teh1****!!!!!-ChatGPT Solution------------------')
# def heita_noppaa():
#     return random.randint(1, 6)
#
# def paaohjelma():
#     heitto = heita_noppaa()
#     while heitto != 6:
#         print("Heitto:", heitto)
#         heitto = heita_noppaa()
#     print("Kuutonen saatiin!")
#
# # Kutsutaan pääohjelmaa
# paaohjelma()
# print('-------------------6_teh2-----------------------')
# num = []
# def randomValue(num):
#     return random.randint(1,num)
# def mainProg():
#     cube = int(input('Cube size: '))
#     search = int(input('Enter the search value: '))
#     while True:
#         number = int(randomValue(cube))
#         num.append(number)
#     # print('The number', number)
#         if number == search:
#             print('Bingo, You got six ')
#             break
#     for i in range (len(num)):
#         print('the numbers ', num)
#         break
# mainProg()
# print('-------------------6_teh2****!!!!!-ChatGPT Solution------------------')
#
# import random
#
# def heita_noppaa(tahkojen_maara):
#     return random.randint(1, tahkojen_maara)
#
# def paaohjelma():
#     tahkojen_maara = int(input("Syötä nopan tahkojen yhteismäärä: "))
#     maksimisilmaluku = int(input("Syötä nopan maksimisilmäluku: "))
#
#     heitto = heita_noppaa(tahkojen_maara)
#     while heitto != maksimisilmaluku:
#         print("Heitto:", heitto)
#         heitto = heita_noppaa(tahkojen_maara)
#     print("Maksimisilmäluku", maksimisilmaluku, "saatiin!")
#
# # Kutsutaan pääohjelmaa
# paaohjelma()
#
# print('-------------------6_teh3-----------------------')
# def bensa(gal):
#     return  gal*3.785
# def mainProgram():
#     while True:
#         gal = float(input('Enter gallon: '))
#         if (gal < 0.0):
#             print('not allowed, BYE')
#             break
#         else:
#             lit = bensa(gal)
#             print(gal,' gallon is equal to: ', lit)
# mainProgram()

# # print('-------------------6_teh3****!!!!!-ChatGPT Solution------------------')
# def muunna_gallonat_litroiksi(gallonat):
#     litrat = gallonat * 3.785
#     return litrat
#
# def paaohjelma():
#     while True:
#         gallonat = float(input("Syötä bensiinin määrä gallonoina (negatiivinen lopettaa): "))
#         if gallonat < 0:
#             break
#         litrat = muunna_gallonat_litroiksi(gallonat)
#         print(gallonat, "gallonaa on", litrat, "litraa.")
#
# # Kutsutaan pääohjelmaa
# paaohjelma()
# print('-------------------6_teh4-----------------------')
#
# def sumList(aList):
#     summa = sum(aList)
#     return summa
# def mainApp():
#     number = [2,4,5,9,11]
#     sum = sumList(number)
#     print("here is the sum: ", sum)
#
# mainApp()

# print('-------------------6_teh5-----------------------')
#
# def paritonList(alist):
#     num = []
#     for i in range (0, len(alist)):
#         if alist[i] % 2 ==0:
#             num.append(alist[i])
#     return num
#
# def mainProg():
#     myList = [2,4,5,6,7, 9, 10]
#
#     print('Here is the list without odd number : ', paritonList(myList))
#     print('The original list: ', myList)
#
# mainProg()

# print('-------------------6_teh5****!!!!!-ChatGPT Solution------------------')
# def karsi_parittomat(lista):
#     uusi_lista = [luku for luku in lista if luku % 2 == 0]
#     return uusi_lista
#
# def main():
#     # Luodaan lista kokonaislukuja
#     alkuperainen_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#     # Kutsutaan funktiota karsi_parittomat ja tallennetaan tulos uuteen listaan
#     karsittu_lista = karsi_parittomat(alkuperainen_lista)
#
#     # Tulostetaan alkuperäinen lista
#     print("Alkuperäinen lista:")
#     print(alkuperainen_lista)
#
#     # Tulostetaan karsittu lista
#     print("Karsittu lista (parilliset luvut):")
#     print(karsittu_lista)
#
# if __name__ == "__main__":
#     main()

print('-------------------6_teh6-----------------------')
#
# def pizza(cent, price):
#     area = math.pi * ((cent / 2)**2)
#     unitPrice = price / area
#     return unitPrice
#
# def mainProg():
#     centForFirstSlice = float(input('Enter the first  pizza slice: '))
#     priceForFirstSlice = float (input('hinta in (€): '))
#
#     centForSecondSlice = float(input('Enter the second pizza slice: '))
#     priceForSecondSlice = float(input('hinta in (€): '))
#     total1 = pizza(centForFirstSlice, priceForFirstSlice)
#     total2 = pizza(centForSecondSlice, priceForSecondSlice)
#
#     if total1 < total2:
#         print('the first price is cheaper ', total1)
#     elif total1 > total2:
#         print(f'the second price is cheaper ', total2)
#     else:
#         print('no difference in the price')
#
# mainProg()

# print('-------------------7_teh1-----------------------')
# def searchMonth(monthNo):
#     season = ("Win", "Win", "Spr", "Spr", "Spr", "Sum", "Sum", "Sum", "Fal", "Fal", "Fal", "Win")
#     return season[monthNo-1]
#
# def mainProg():
#     index= int(input('enter the month number (1-12): '))
#     season = searchMonth(index)
#     print (" the season is ", season)
# mainProg()
# print('-------------------7_teh1****!!!!!-ChatGPT Solution------------------')
# def hae_vuodenaika(kuukausi):
#     vuodenajat = (
#         "talvi", "talvi", "kevät", "kevät", "kevät",
#         "kesä", "kesä", "kesä", "syksy", "syksy",
#         "syksy", "talvi"
#     )
#     return vuodenajat[kuukausi - 1]
#
# def main():
#     kuukausi = int(input("Syötä kuukauden numero (1-12): "))
#     vuodenaika = hae_vuodenaika(kuukausi)
#     print("Kuukausi {} on {}".format(kuukausi, vuodenaika))
#
# if __name__ == "__main__":
#     main()
# print('-------------------7_teh2-----------------------')
# def addName():
#     nimi = []
#
#     while True:
#         name = str(input("Enter your name: "))
#         if name == "":
#             break
#         if name in nimi:
#             print('Exist ')
#         else:
#             print('new name ', name)
#             nimi.append(name)
#     print('add new name: ')
#     for name in nimi:
#         print(nimi)
#
# addName()
# print('-------------------7_teh3-----------------------')
# lentoAsema = []
#
# def lentoOpe(userIn):
#     if userIn == "haku":
#         lentoId= int(input('Here is the Airport ID: '))
#         for i in range(0,len(lentoAsema)):
#             if lentoNo== lentoAsema:
#                 Print('the details: ')
#     if userIn == "append":
#         lentoId = int(input('enter the Airport id: '))
#         lentoAsema.append(lentoId)
#         print('The airport added')
#     if userIn == "delete":
#         lentoId = int(input('enter the Airport id to remove: '))
#         lentoAsema.remove(lentoId)
#         print(' the airport is removed')
#     if userIn == "print":
#         print('Here is the list, ', lentoAsema)
# def mainProf():
#     while True:
#         userInput= str(input('What do you want: '))
#         if userInput == "":
#             break
#         lentoOpe(userInput)
# mainProf()

# print('-------------------7_teh1****!!!!!-ChatGPT Solution------------------')
# def lisaa_lentoasema(lentoasemat):
#     icao_koodi = input("Syötä lentoaseman ICAO-koodi: ")
#     nimi = input("Syötä lentoaseman nimi: ")
#     lentoasemat[icao_koodi] = nimi
#     print("Lentoasema tallennettu.")

# def hae_lentoasema(lentoasemat):
#     icao_koodi = input("Syötä lentoaseman ICAO-koodi: ")
#     if icao_koodi in lentoasemat:
#         print("Lentoaseman nimi: ", lentoasemat[icao_koodi])
#     else:
#         print("Lentoasemaa ei löytynyt.")

# def main():
#     lentoasemat = {}
#
#     while True:
#         print("\nValitse toiminto:")
#         print("1. Lisää uusi lentoasema")
#         print("2. Hae lentoaseman tiedot")
#         print("3. Lopeta")
#
#         valinta = input("Syötä valintasi (1-3): ")
#
#         if valinta == "1":
#             lisaa_lentoasema(lentoasemat)
#         elif valinta == "2":
#             hae_lentoasema(lentoasemat)
#         elif valinta == "3":
#             break
#         else:
#             print("Virheellinen valinta. Valitse uudelleen.")
#
#     print("Ohjelma lopetettu.")
#
# if __name__ == "__main__":
#     main()

print('-------------------8_teh1-----------------------')

