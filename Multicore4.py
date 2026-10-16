import multiprocessing,time,os
def SumCube(no):
   print(f"processing is running with PID : {os.getpid()}")
   Sum=0
   for i in range(1,no+1):
      Sum=Sum+(i**3)  #it can be written are i*i*i

   return Sum

def main():
 Data=[10000000,20000000,30000000,40000000,50000000]
 Result=list()
 Start_time=time.perf_counter()
 pobj=multiprocessing.Pool()
 Result=pobj.map(SumCube,Data)
 pobj.close()
 pobj.join()
 End_time=time.perf_counter()
 
 print(f"Result is ")
 print(Result)   
 print(f"Total time required {End_time-Start_time:.4f} Seconds ")
if __name__ == "__main__":
    main()