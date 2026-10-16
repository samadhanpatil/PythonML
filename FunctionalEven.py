checkEven = lambda no:(no%2==0)

def main():
 Value=int(input("Enter number :"))
 Ret=checkEven(Value)
 if (Ret == True):
   print("Ret is  even")
 else:
   print("Ret is odd")
if __name__=="__main__":
 main()

 ##This is called hybrid procedural approach, because functional program - def and inline function is gettinb used