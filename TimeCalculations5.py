import time 

def factorial(val1):
   fact=1
   for i in range(1,val1+1):
       fact=fact*i
   return fact
   


def main():
    no=int(input("enter number for factorial"))
    start_time=time.perf_counter()

    ret = factorial(no)

    end_time=time.perf_counter()
    print(f"Factorial of {no} number is {ret}")
    print(f"Time required to complete is : {end_time-start_time:.5f} seconds")

if __name__=="__main__":
    main()