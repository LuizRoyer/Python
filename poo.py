
#classe
class Veiculo:
    def move(self):
        print(f'{self.get_name()} Movendo-se ' )

    #metodo construtor
    def __init__(self,name,year ,color):
        #para atributo privado utilizar __
        self.__name = name
        self.__year = year
        self.__color = color
        self.model = None

    #getter
    def get_name(self):
        return self.__name 
    
    #setter
    def set_name(self, value):
        self.__name = value


#herança 
class Moto (Veiculo):
    #metodo init sera herdado

    def move(self):
        print(f'{self.get_name()} ligando os motores ' )


class Barco (Veiculo):
    def move(self):
        print(f'{self.get_name()} Navegando ' )


class Aviao (Veiculo):
    def __init__(self, name, year, color, power):
        super().__init__(name, year, color)
        self.__power = power
    def move(self):
        print(f'{self.get_name()} voando ' )

if __name__ == '__main__':

    fusca = Veiculo('fusca', 1976, 'branco')  
    fusca.model ='VW'    
    print(fusca.model)
    fusca.move()

    gol = Veiculo('gol', 2000, 'verde')
    gol.get_name()
    gol.move()
    gol.set_name('G4')
    gol.move()

    cg = Moto('cg', 2000, 'prata')
    cg.model = 'Yamaha'
    cg.move()

    barco = Barco('barco', 2022, 'azul')
    barco.move()

    caca = Aviao('caca', 2022, 'preto', 1000)
    caca.move()