def fileRead(fileName):
  
       f=open(fileName,'r')
       content=f.readline(12)
       print(content)


print("Reading only 12 bits")
fileRead('InputTxt.txt')
