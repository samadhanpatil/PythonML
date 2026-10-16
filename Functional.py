addition = lambda No1,No2:No1+No2

Substract = lambda No1,No2:No1-No2


print("Enter first no ")
No1=int(input())
print("Enter Second no ")
No2=int(input())

Ret1=addition(No1,No2)
Ret2=Substract(No1,No2)
print(f"Addition is {Ret1}")
print(f"Substraction is {Ret2}")