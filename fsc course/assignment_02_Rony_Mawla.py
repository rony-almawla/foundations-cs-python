##QUESTION 1:
def countDigits():
  number = input("Enter any number greater than zero: ")
  numberm = int(number)
  if(numberm < 10 ):
    return 1
  else: 
    count = 0
    while(numberm>9):
      count=count+1
      numbern=numberm//10
  print("The number of digits in the number are: ",count)
    
# countDigits();

##QUESTION 2:
def findMax():
  list1 = []
  number = input("Enter any numbers you want")
  print(len(number))
  for i in range(0, len(number)):
    print(i)
    list1.append(number[i])
  if len(list1) == 1:
    return number
  else :
    # len(list1) > 1
    list2 = sorted(list1)
    print(list2[-1])
# findMax();
  

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

main();