import os 
def SumCube(no):
   Sum=0
   for i in range(1,no+1):
      Sum=Sum+(i*i*i)  #it can be written are i*i*i
   return Sum

def main():
 Ret=SumCube(5)
 print(f"Result is {Ret}")
    
if __name__ == "__main__":
    main()