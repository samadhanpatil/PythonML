def addition(No1,No2):
 return No1+No2

def Substract(No1,No2):
 return No1-No2


print("Enter first no ")
No1=int(input())
print("Enter Second no ")
No2=int(input())

Ret1=addition(No1,No2)
Ret2=Substract(No1,No2)
print(f"Addition is {Ret1}")
print(f"Substraction is {Ret2}")