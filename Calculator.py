#  <--------------------------------------Calculator----------------------------------->

#function
def addition (num1,num2):
    result = num1+num2#num1-value+num2-value=result
    print("Answer is : {0} + {1} = {2}\n".format(num1,num2,result))

def substraction (num1,num2):
    result = num1+num2#num1-value-num2-value=result
    print("Answer is : {0} - {1} = {2}\n".format(num1,num2,result))
    
    
def multiplication (num1,num2):
    result = num1*num2#num1-value*num2-value=result
    print("Answer is : {0} × {1} = {2}\n".format(num1,num2,result))


def division (num1,num2):
    if num2==0.0:
        print("Opps! can't divide by zero.")
    else:
        result = num1/num2
        print("Answer is : {0} ÷ {1} = {2}\n".format(num1,num2,result))


while True:

#Display    
    print("What do you want to do?")
    print("------------------------------")
    print("Press 1 for addition (+) ")
    print("Press 2 for Substraction (-) ")
    print("Press 3 for Multiplication (×) ")
    print("Press 4 for Division (÷) ")
    print("Enter 'Q' or 'q' for Exit ")


#User Input for choice
    choice = input("Press your choice to continue : ")
 
#Conditon of to Exit calculator
    if choice == 'Q' or choice == 'q':
        break

#Taking two number as a input from user
    num1=float(input("Enter First number : "))
    num2=float(input("Enter Second number : "))



#Condition
    if choice == '1':
        addition(num1, num2)
    elif choice == '2':
        substraction(num1, num2)
    elif choice == '3':
        multiplication(num1, num2)
    elif choice == '4':
        division(num1, num2)
    else:
        print("Invalid choice!")



    

