# QUESTION 1:
def countDigits():
  number = input("Enter any number greater than zero")
  number = int(number)
  if(number < 10 ):
    return 1
  else: 
    count = 0
    while(number>9):
      count=count+1
      number=number//10
  print("The number of digits in the number are:",count)
    
countDigits();

# QUESTION 2:
def findMax():
  list1 = []
  number = int(input("Enter any numbers you want"))
  for i in range(0, number):
    list1.append(number)
  if list1.len() == 1:
    return input
  else :
    list1.len() > 1
    list2 = list1.sort()
    return(list2.len -1)
findMax();
  

def main():
  num = int(input("Choose a number between 1 till 4"))
  if num == 1:
    countDigits()
  elif num ==2 : 
    findMax()
  elif num ==3:
    countTags()
  elif num == 4:
    exit()
  else : 
    print("please choose a number between 1 to 4")