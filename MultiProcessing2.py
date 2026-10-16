import time
import multiprocessing
import os
def SumEven(No):
 print(f"PID of SumEven {os.getpid()} PPID of Parent is {os.getppid()}")
 sum=0
 for i in range(2,No,2):
    sum=sum+i
 print("Summation of Even :",sum) 
def SumOdd(No):
 print(f"PID of SumOdd {os.getpid()} PPID of Parent is {os.getppid()}")
 sum=0
 for i in range(1,No,2):
    sum=sum+i  
 print("Summation of Odd :",sum) 
def main():
   print(f"PID of Main {os.getpid()} PPID of Parent is {os.getppid()}")
   start_time=time.perf_counter()
   tobj1=multiprocessing.Process(target=SumEven,args=(10000000,))
   tobj2=multiprocessing.Process(target=SumOdd,args=(10000000,))
   tobj1.start()
   tobj2.start()
   tobj1.join()
   tobj2.join()

   end_time=time.perf_counter()
   print(f"Time required is {end_time-start_time:.4f}")
if __name__=="__main__":
    main()