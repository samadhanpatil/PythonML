class Demo:
  #Class variables
  Value1=10
  Value2=20

  def __init__(self):  #Constructor Method
   self.No1=11
   self.No2=21
  
  def fun(self):
   print(f"Inside instance method fun")
   print(self.No1)
   print(self.No2)
   print(Demo.Value1)
   print(Demo.Value2) # it should be use while accessing class variable
 
  @classmethod
  def gun(cls):
   print(f"Inside Class method gun")
  #  print(Demo.No1)
  #  print(Demo.No2)  Not allowed accessing using giving call name
   print(cls.Value1)
   print(cls.Value2)

#Call with object
dobj=Demo()
dobj.gun()