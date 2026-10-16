no=11  #Global variable
def display():
 global no
 no=21
 print("From display no:",no)    

print("Before : ",no)
display()
print("After :",no)
