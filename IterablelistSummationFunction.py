
def Summation(Data):
  A=0
  for i in Data:
   A=A+i
  #print("Sum of no is :",A)
  return A  
def main():
  marks=[78,90,56,98,77]
  Ret=Summation(marks)
  print("Sum of nu is :",Ret)
if __name__=="__main__":
    main()