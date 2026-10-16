from functools import reduce
CheckEven = lambda No:(No%2 ==0)
Increment = lambda No: No+1
addition = lambda No1,No2: No1+No2

def main():
 Data=[13,12,8,10,11,20]
 print("Inputdata is :",Data)
 FData=list(filter(CheckEven,Data))
 MData=list(map(Increment,FData))

 RData=reduce(addition,MData)

 print("Data after filter :",FData)
 print("Data after map ",MData)
 print("Data after Reduce ",RData)


if __name__=="__main__":
 main()

"""
Best example of Filter. Map, reduce is creating chinese dish
Select veggie--> chop (map-mix)-->Dish ready --Reduce
"""