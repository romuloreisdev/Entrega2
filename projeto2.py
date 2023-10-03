#from my_libraries.shapes2d import Point, Circle
#from my_libraries.coordsystems import CartesianBoard
#import time


#não consegui entender essas bibliotecas

def areacirculo():

    r=float(input("Insira a medida do raio: "))
    area=3.14*r*r
    print("area do círculo é: ", area)


def areatriangulo():
  base=float(input("Insira a medida da base: "))
  altura=float(input("Insira a medida da altura: "))
  area=(base*altura)*0.5 
  print("area do trinângulo é: ", area)


def areaquadrado():
  lado=float(input("Insira a medida do lado: "))
  area=lado*lado 
  print("area do quadrado é: ", area)

def arearetangulo():
  base=float(input("Insira a medida da base: "))
  altura=float(input("Insira a medida da altura: "))
  area=base*altura  
  print("area do retângulo é: ", area)

while True:

    print("\n Escolha uma opção: \n 1 - Círculo \n 2 - Triângulo \n 3 - quadrado \n 4 - retângulo \n 0 - sair")
    escolha=int(input("número? ")) 

    if escolha==1:areacirculo()
    elif escolha==2:areatriangulo()
    elif escolha==3:areaquadrado()
    elif  escolha==4:arearetangulo()
    elif  escolha==0:break