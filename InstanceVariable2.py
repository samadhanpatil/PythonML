class Marvellous:
 #class variable
 No1=11
 No2=12
 def __init__(self):
  #instance variable
  self.value1=21
  self.value2=51   #instance variable, In python if we need instance variable then __init__ method. No choice
 
  

#  def __del__(self):
#   print("Inside Destructor")

print(Marvellous.No1)
print(Marvellous.No2)
#Object or instance creation 
Mobj1=Marvellous()  
Mobj2=Marvellous()  
Mobj3=Marvellous()  

print(Mobj1.value1)
print(Mobj2.value1)
print("End of Application")