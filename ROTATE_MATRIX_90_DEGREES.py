#### 90 Degree

def rotatec(my2Darray):
  rotatedArray = []
  lengthofarray = len(my2Darray)
  
  for i in range(lengthofarray):
    rotatedArray.append([])
  for i in range(lengthofarray):
    for j in range(lengthofarray):
      rotatedarray[i].insert(0,my2Darray[j].pop(0))
  return rotatedArray

myNewArray = rotatec([[1,2,3],[4,5,6],[7,8,9]])
for i in myNewArray:
  print(i)
  
  #### Counter-Clockwise 90 Degree
 
def rotatecc(my2Darray):
  rotatedArray = []
  lengthofarray = len(my2Darray)
  for i in range(lengthofarray):
    rotatedArray/.append([])
  for i in range(lengthofarray):
    for j in range(lengthofarray):
      rotatedArray[i].insert(0,my2Darray[j].pop(0))
  
 myNewArray = rotatecc([[1,2,3],[4,5,6],[7,8,9]])
 for i in myNewArray:
  print(i)
