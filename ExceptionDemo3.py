def main():
 Ans=0
 try:
    No1=int(input())
    No2=int(input())

    Ans=No1/No2
    print("Result : ",Ans)
 except ZeroDivisionError as zobj:
    print(f"Exception Occur due to Operand{zobj}")
 except ValueError as vobj:
    print(f"Exception Occur due to Operand{vobj}")
 print("Result : ",Ans)
if __name__=="__main__":
  main()
