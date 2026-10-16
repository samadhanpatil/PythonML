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
    SumEven(200000)
    SumOdd(200000)
if __name__=="__main__":
    main()