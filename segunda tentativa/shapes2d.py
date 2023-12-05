import math

class Point():
    def __init__(self, n, x, y):
        self._n = n
        self._x = x
        self._y = y

    def updateCoord(self, x, y):
        self._x = x
        self._y = y

    def getType(self):
        return 'Point_'

    def getNumber(self):
        return self._n

    def printCoord(self):
        print(f'\nO ponto {self._n} possui as coord: ({self._x}, {self._y}).')


class Circle(Point):
    def __init__(self, n, x, y, radius):
        super().__init__(n, x, y)
        self.radius = radius

    def getType(self):
        return 'Circle_'

    def updateCoord(self, x, y, radius):
        super().updateCoord(x, y)
        self.radius = radius

    def printCoord(self):
        print(f'\nO círculo {self._n} possui origem em: ({self._x}, {self._y})')
        print(f'E o seu raio é {self.radius}')

    def pointIn(self, x_ponto, y_ponto):
        # Calcula a distância entre o ponto e o centro do círculo
        distance = math.sqrt((x_ponto - self._x)**2 + (y_ponto - self._y)**2)

        # Verifica se a distância é menor ou igual ao raio
        if distance <= self.radius:
            print("O ponto está dentro do círculo.")
        else:
            print("O ponto está fora do círculo.")
        return distance 

    def area(self):
        # Calcula a área deste círculo e mostra no terminal
        area = 3.14 * self.radius * self.radius
        return area

    def perimeter(self):
        # Calcula o perímetro deste círculo e mostra no terminal
        perimeter = 2 * 3.14 * self.radius
        return perimeter

    def my_function(self):
        """ Defina mais funções de seu interesse aqui"""
        pass


class Line():
    """ Implementar a linha com dois pontos internos"""     
    """ Definir funções membro e quaisquer outros atributos da classe"""
    pass


class SuaOutraForma():
    """ Defina quantas formas quiser utilizando as relações de herança"""
    pass


# Teste da classe Point
point1 = Point(1, 2, 3)
point1.printCoord()
point1.updateCoord(4, 5)
point1.printCoord()

# Teste da classe Circle
circle1 = Circle(1, 0, 0, 5)
circle1.printCoord()
print(f'Área do círculo: {circle1.area()}')
print(f'Perímetro do círculo: {circle1.perimeter()}')
print(circle1.pointIn(10, 4))  # Verifica se o ponto (3, 4) está dentro do círculo

# Teste da classe Line (ainda não implementada)
line1 = Line()

# Teste da classe SuaOutraForma (ainda não implementada)
forma1 = SuaOutraForma()
