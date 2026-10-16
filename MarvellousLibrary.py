def filterX(Task,Elements):
  Result=list()
  for i in Elements:
     Ret=Task(i)  #CheckEven
     if(Ret==True):
      Result.append(i)
 
  return Result


def mapX(Task,Elements):
  Result=list()
  for i in Elements:
     
     Ret=Task(i)  #CheckEven
     Result.append(i)
 
  return Result

def ReduceX(Task,Elements):
  
  Sum=0
  for i in Elements:
     Sum=Task(Sum,i)  #CheckEven
    
  return Sum
