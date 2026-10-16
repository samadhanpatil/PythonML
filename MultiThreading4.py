import threading 

def evendisplay(val1,val2,val3):
 print(f"Inside display ,{val1},{val2},{val3}",threading.get_ident())

# def odddisplay(val1):
#    if val1%2!=0:
#       return True
   
  
def main():
  print("Inside main :",threading.get_ident())
  tobj1=threading.Thread(target=evendisplay,args=(11,21,51,))   #This is tuple because args accept iterable input. Otherwise error i
  tobj1.start()
  # tobj2=threading.Thread(target=odddisplay,args=3)
  # tobj2.start()
if __name__=="__main__":
    main()