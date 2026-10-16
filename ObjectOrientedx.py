class Arithmatic:
 def addition(self,No1,No2):
  return No1+No2

 def Substract(self,No1,No2):
  return No1-No2
    
Aobj=Arithmatic()

print("Enter first no ")
No1=int(input())
print("Enter Second no ")
No2=int(input())

Ret1=Aobj.addition(No1,No2) 
Ret2=Aobj.Substract(No1,No2)
print(f"Addition is {Ret1}")
print(f"Substraction is {Ret2}")


