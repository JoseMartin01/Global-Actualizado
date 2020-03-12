import abc

#
# Product A
# products implement the same interface so that the classes can refer
# to the interface not the concrete product
#
class ProductoSamsung:
    @abc.abstractmethod
    def getTelefonoSamsung(self):
        pass
    @abc.abstractmethod
    def getTabletSamsung(self):
        pass

#
# ConcreteProductAX and ConcreteProductAY
# define objects to be created by concrete factory
#
class TelefonoSamsung(ProductoSamsung):
  def getTelefonoSamsung(self):
    return "TelefonoSamsung"

  def getImagen(self):
      return "./imagenes/sgFold.jpg"

class TabletSamsung(ProductoSamsung):
  def getTabletSamsung(self):
    return "TabletSamsung"

  def getImagen(self):
    return './imagenes/galaxyTabS4.jpg'

#
# Product B
# same as Product A, Product B declares interface for concrete products
# where each can produce an entire set of products
#
class ProductoApple:
    @abc.abstractmethod
    def getTelefonoApple(self):
        pass
    @abc.abstractmethod
    def getTabletApple(self):
        pass
#
# ConcreteProductBX and ConcreteProductBY
# same as previous concrete product classes
#
class TelefonoApple(ProductoApple):
  def getTelefonoApple(self):
    return "TelefonoApple"

  def getImagen(self):
      return './imagenes/iphone11.jfif'

class TabletApple(ProductoApple):
  def getTabletApple(self):
    return "TabletApple"

  def getImagen(self):
      return './imagenes/ipad6.jpg'

#
# Abstract Factory
# provides an interface for creating a family of products
#
class ElectronicaFactory:
    @abc.abstractmethod
    def createTelefono(self):
        pass
    @abc.abstractmethod
    def createTablet(self):
        pass
    
#
# Concrete Factories
# each concrete factory create a family of products and 
# client uses one of these factories
#
class SamsungFactory(ElectronicaFactory):
  def createTelefonoSamsung(self):
    return TelefonoSamsung()

  def getImagen(self):
      return './imagenes/sgFold.jpg'
  
  def createTabletSamsung(self):
    return TabletSamsung()

  def getImagen(self):
    return './imagenes/galaxyTabS4.jpg'

     
class AppleFactory(ElectronicaFactory):
  def createTelefonoApple(self):
    return TelefonoApple()

  def getImagen(self):
      return './imagenes/iphone11.jfif'
  
  def createTabletApple(self):
    return TabletApple()

  def getImagen(self):
      return './imagenes/ipad6.jpg'

  
if __name__ == "__main__":
  samsungFactory = SamsungFactory()
  appleFactory = AppleFactory()
  
  p1 = samsungFactory.createTelefonoSamsung()
  print("Product: " + p1.getTelefonoSamsung())
  p1 = samsungFactory.createTabletSamsung()
  print("Product: " + p1.getTabletSamsung())

  p2 = appleFactory.createTelefonoApple()
  print("Product: " + p2.getTelefonoApple())
  p2 = appleFactory.createTabletApple()
  print("Product: " + p2.getTabletApple())
