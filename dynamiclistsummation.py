def summation(Data):
 sum=0
 for i in Data:
    sum=sum+i
 return sum   

def main():
  size=0
  Arr=list()
  print("enter the number of elements :")
  size=int(input())
  print("Enter the elements")
  for i in range(size):
     no=int(input())
     Arr.append(no)
  Ret=summation(Arr)
  print("Summation of list is :",Ret)
if __name__=="__main__":
    main()