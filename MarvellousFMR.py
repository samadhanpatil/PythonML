from functools import reduce

def filterX(Task,Elements):
  Result=list()
  for i in Elements:
     Ret=Task(i)  #CheckEven
     if(Ret==True):
      Result.append(i)
 
  return Result


def mapX(Task,Elements):
  Result=list()
  for i in Elements:
     Ret=Task(i)  #CheckEven
     Result.append(i)
 
  return Result

def ReduceX(Task,Elements):
  
  Sum=0
  for i in Elements:
     Sum=Task(Sum,i)  #CheckEven
    
  return Sum



CheckEven = lambda No:(No%2 ==0)
Increment = lambda No: No+1
addition = lambda No1,No2: No1+No2

def main():
 Data=[13,12,8,10,11,20]
 print("Inputdata is :",Data)
 FData=list(filterX(CheckEven,Data))
 MData=list(mapX(Increment,FData))

 RData=ReduceX(addition,MData)

 print("Data after filter :",FData)
 print("Data after map ",MData)
 print("Data after Reduce ",RData)


if __name__=="__main__":
 main()

"""
Best example of Filter. Map, reduce is creating chinese dish
Select veggie--> chop (map-mix)-->Dish ready --Reduce
"""