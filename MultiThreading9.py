import time,threading
def SumEven(No):
    print("TID Of SumEven thread is :",threading.get_ident())
def SumOdd(No):
    print("TID Of SumOdd thread is :",threading.get_ident())
def main():
   print("TID Of main thread is :",threading.get_ident())
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