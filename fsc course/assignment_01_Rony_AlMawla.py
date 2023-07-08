###QUESTION 1:

def factorial(n): 
	fact=1 
	for i in range(1,n+1): 
		fact=fact*i 
	return fact 
  
n=int(input("Enter positive number 'N': ")) 
f=factorial(n) 
print('Factorial is: ',f) 


####QUESTION 2:
def divisor_number():
  number = input(int("Enter a number: "))
  list = []
  for divisors in range (1, number+1):
    if number % divisors ==0:
      list.append(divisors)
      print(list)


 #####QUESTION 4:
def list_integers():
  list = []
  number = input("Enter any number you want")
  number = int(number)
  if number % 2 == 0:
    list.append()
    print(list)
list_integers()



#####question 5:


    #function for checking if length password>8
    def check_length(pwd):
        if len(pwd)>=8:     
            print("Strong Password")
        else:
            print("length is less than 8")
        return pwd
    for password in passwords_lst:  #testing with actual list
        print(check_length(password))

	
	def check_specialchar(pwd):
        spec_char_lst=['$','#','@','.','!','?','<','>']
        result=any(elem in spec_char_lst for elem in pwd)
        if result is True:
            print("Has special charactrs")
        else: 
            print("No special characters")
        return pwd
    for password in passwords_lst: #testing with actual list
        print(check_specialchar(password))



    #function for checking if password has at uppecase
    def checkifUpper(pwd):
        for char in pwd:
            if char.isUpper() is true:
                print("Has Uppercase letters")
            else:
                #print("No special characters")
        return pwd
    for password in passwords_lst:

        print(checkif_digit(password))

#function for calling all three tests/functions created above and checking if passwords meet all three conditions
def check_pwd(pwd):
    for element in pwd:

    return element
print(check_pwd(passwords_lst))


