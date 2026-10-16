class Base:
 def __init__(self):
  print(f"inside base constructor")

 def fun(self):
  print(f"Inside base fun")

class Derived(Base):
 def __init__(self):
  super().__init__()
  print("Inside derived constructor")

dobj=Derived()
dobj.fun()