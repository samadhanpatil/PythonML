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
   print(self.Value1)
   print(self.Value2)
 
dobj=Demo()  #immediate constructor get called here
dobj.fun()