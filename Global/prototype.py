from abc import ABC, abstractmethod

class MousePrototype(ABC):
    color='Blanco'
    marca='Apple'
    @abstractmethod
    def crear(self):
        pass        
        
    @abstractmethod
    def clonar(self):
        pass

class MouseAlambrico(MousePrototype):
    """
    Implement a behavior associated with a state of the Context.
    """
    def __init__(self):
        self.imagen = "./imagenes/mouseAlambrico.jpg"
    
    def crear(self):
        print('Color: ',MousePrototype.color)
        print('Marca: ',MousePrototype.marca)
        print("Crear mouse alambrico")

    def clonar(self):
        print('Color: ',MousePrototype.color)
        print('Marca: ',MousePrototype.marca)
        print("Clonar mouse alambrico")


class MouseInalambrico(MousePrototype):
    """
    Implement a behavior associated with a state of the Context.
    """
    def __init__(self):
        self.imagen = "./imagenes/mouseInalambrico.jfif"

    def crear(self):
        print('Color: ',MousePrototype.color)
        print('Marca: ',MousePrototype.marca)
        print("Crear mouse inalambrico")


    def clonar(self):
        print('Color: ',MousePrototype.color)
        print('Marca: ',MousePrototype.marca)
        print("Clonar mouse inalambrico")


if __name__ == "__main__":
  mouseAlambrico = MouseAlambrico()
  mouseAlambrico.crear()
  mouseAlambrico = MouseAlambrico()
  mouseAlambrico.clonar()
  
  mouseInalambrico = MouseInalambrico()
  mouseInalambrico.crear()
  mouseInalambrico = MouseInalambrico()
  mouseInalambrico.clonar()



