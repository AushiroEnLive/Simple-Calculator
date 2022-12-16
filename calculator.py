#Import
import time
#Définitions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   return x / y
#Code
print("1.Addition") 
print("2.Soustraction")
print("3.Multiplication")
print("4.Division")
time.sleep(1)
choix = input("Entrer un choix (1/2/3/4):")

numero1 = int(input("Entrer le premier nombre: "))
time.sleep(1)
numero2 = int(input("Entrer le second nombre: "))

if choix == '1':
   print(numero1,"+",numero2,"=", add(numero1,numero2))

elif choix == '2':
   print(numero1,"-",numero2,"=", subtract(numero1,numero2))

elif choix == '3':
   print(numero1,"*",numero2,"=", multiply(numero1,numero2))

elif choix == '4':
   print(numero1,"/",numero2,"=", divide(numero1,numero2))
else:
   print("Erreur : Choix Invalide")
#Fin du code
print("By AushiroEnLive")