class Arithmatic:
 
 def __init__(self,A,B):  #Constructor Method
  self.No1=A
  self.No2=B
 #Methos which is having first self word it instance method
 def addition(self):
  return self.No1+self.No2

 def Substract(self):
  return self.No1-self.No2
    


print("Enter first no ")
No1=int(input())
print("Enter Second no ")
No2=int(input())

Aobj=Arithmatic(No1,No2)

Ret1=Aobj.addition() 
Ret2=Aobj.Substract()
print(f"Addition is {Ret1}")

print(f"Substraction is {Ret2}")


