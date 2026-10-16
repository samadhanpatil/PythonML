class Arithmatic:
 def addition(No1,No2):
  return No1+No2

 def Substract(No1,No2):
  return No1-No2
    
Aobj=Arithmatic()

print("Enter first no ")
No1=int(input())
print("Enter Second no ")
No2=int(input())

#Ret1=addition(Aobj,No1,No2) --Actual Execution of method is done like this. 
#TypeError: Arithmatic.addition() takes 2 positional arguments but 3 were given

Ret1=Aobj.addition(No1,No2) 
Ret2=Aobj.Substract(No1,No2)
print(f"Addition is {Ret1}")
print(f"Substraction is {Ret2}")


