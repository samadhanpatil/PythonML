import time,threading
def SumEven(No):
 sum=0
 for i in range(2,No,2):
    sum=sum+i
 print("Summation of Even :",sum) 
def SumOdd(No):
 sum=0
 for i in range(1,No,2):
    sum=sum+i  
 print("Summation of Odd :",sum) 
def main():
   start_time=time.perf_counter()
   
   tobj1=threading.Thread(target=SumEven,args=(10000000,))
   tobj2=threading.Thread(target=SumOdd,args=(10000000,))
   tobj1.start()
   tobj2.start()
   tobj1.join()
   tobj2.join()

   end_time=time.perf_counter()
   print(f"Time required is {end_time-start_time:.4f}")
if __name__=="__main__":
    main()