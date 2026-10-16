def checkEven(no):
  if (no%2==0):
    return True
  else:
    return False

def main():
 Value=int(input("Enter number :"))
 Ret=checkEven(Value)
 if (Ret == True):
   print("Ret is  even")
 else:
   print("Ret is odd")
if __name__=="__main__":
 main()