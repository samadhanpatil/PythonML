class Base1:
 def fun(self):
  print(f"Inside Base1 fun")
class Base2:
 def gun(self):
  print(f"Inside Base2 gun")

class Derived(Base1,Base2):
 def sun(self):
  print(f"Inside dervied Sun")

dobj=Derived()
dobj.fun()
dobj.gun()
dobj.sun()