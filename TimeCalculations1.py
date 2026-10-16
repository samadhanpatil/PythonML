def factorial(val1):
   fact=1
   for i in range(1,val1+1):
       fact=fact*i
   return fact
   


def main():
    no=int(input("enter number for factorial"))
    ret = factorial(no)
    print("Factorial of number is :",ret)
 
if __name__=="__main__":
    main()