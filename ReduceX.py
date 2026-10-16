from functools import reduce
def CheckEven(No):
 return (No%2 ==0)

def Increment(No):
  return No+1

def addition(No1,No2):
   return No1+No2
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
