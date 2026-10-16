from abc import ABC,abstractmethod
class Base(ABC):
 @abstractmethod
 def Addition(self,No1,No2):
  pass

class Dervied(Base):
 pass

dobj=Dervied() #Error 
