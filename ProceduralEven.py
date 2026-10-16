def checkEven(no):
  if (no%2==0):
    print("Number is even")
  else:
   print("Number is odd")

def main():
 Value=int(input("Enter number :"))
 checkEven(Value)
if __name__=="__main__":
 main()