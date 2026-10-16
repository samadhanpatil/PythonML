class Base:
 def fun(self):
  print(f"Inside base fun")

class Derived(Base):
 def sun(self):
  print(f"Inside dervied Sun")

dobj=Derived()
dobj.fun()
dobj.sun()