class Point():

    def __init__(self,n,x,y):
        self._n= n
        self._x= x
        self._y= y


    def updateCoord(self,x,y):
        self._x= x
        self._y= y

    
    def getType(self):
        return 'Point_'
        
        
    def getNumber(self):
        return self._n
    

    def printCoord(self):
        print(f'\nO ponto {self._n} possui as coord: ({self._x}, {self._y}).')        




class Circle(Point):
    
    """ O círculo herda do ponto suas funcionalidades e adiciona raio"""
    """ É necessário definir as funções membro para o círculo operar"""
    
    def __init__(self,n,x,y,radius):
        
        super().__init__(n, x, y)
        self.radius= radius
        
    
    def getType(self):
        """ Atencção!!! Polimorfismo aplicado"""
        return 'Circle_'
        
    
    def updateCoord(self,x,y,radius):
        
        super().updateCoord(x, y)
        self.radius= radius

    
    def printCoord(self):
        
        print(f'\nO círculo {self._n} possui origem em: ({self._x}, {self._y})')
        print(f'E o seu raio é {self.radius}')
        
    
    def pointIn(self,x_ponto, y_ponto, x, y, radius):
    
        # Calcula a distância entre o ponto e o centro do círculo
        distance = math.sqrt((x_ponto - x)**2 + (y_ponto - y)**2)

        # Verifica se a distância é menor ou igual ao raio
        
        if distance(x_ponto, y_ponto, x, y, radius):
            print("O ponto está dentro do círculo.")
        else:
            print("O ponto está fora do círculo.")
        return distance <= radius

    
    def area(self,radius):
        #calcula a área deste circulo e mostra no terminal
        area=3.14*radius*radius
        return area
    
    
    def perimeter(self,radius):
        #calcula o perímetro deste circulo e mostra no terminal
        perimeter=2*3.14*radius
        return perimeter
    
    
    def my_function(self):
        """ defina mais funções de seu interesse aqui"""
        pass
    



class Line():
    
    """ implementar a linha com dois pontos internos"""     
    """ definir funções membro e quaisquer outros atributos da classe""" 
    pass




class SuaOutraForma():

    """ Defina quantas formas quiser utilizando as relações de herança"""
    pass