import numbers


def add():
    num1 = int (input("enter number 1 :"))
    num2 =int (input("enter numbr2:"))
    print("sum of two numbers  :",num1+num2)

def mul():
    num1 = int (input("enter number 1 :"))
    num2 =int (input("enter numbr2:"))
    print("sum of two numbers  :",num1*num2)
    
def sub():
    num1 = int (input("enter number 1 :"))
    num2 =int (input("enter numbr2:"))
    print("sum of two numbers  :",num1-num2) 


while (1):
    n=int (input ("please select\n1. add\n2 mul\n3 sub"))
  
    if(n==1): 
        print ("you have selected addition")
        add()
    elif (n==2):
        print ("you have selected multiplication")
        mul()
    elif (n==3):
        print ("you have selected substraction")
        sub()
      