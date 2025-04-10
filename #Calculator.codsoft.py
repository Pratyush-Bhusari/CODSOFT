#Calculator
print("--welcome to calculator app--")

ch="yes"

while ch.lower() !="no":
    try:
        #input two numbers
        a=int(input("enter first number:"))
        b=int(input("enter second number:"))
        
        #menu for operations
        print ("\n choose an operation:")
        print ("1 addition (+)")
        print ("2 substraction (-)")
        print ("3 multiplication (*)")
        print ("4 division (/)")
        
        operation = input ("enter your choice (1/2/3/4 or  +,-,*,/):")
        #perform the operations
        if operation == '1' or operation == '+':
            print (f"{a} + {b} = {a + b}")
        elif operation == '2' or operation == '-':
            print (f"{a} - {b} = {a - b}")
        elif operation == '3'or operation == '*':
            print (f"{a} * {b} = {a * b}")
        elif operation == '4' or operation == '/':
            if b != 0:
                print (f"{a} / {b} = {a / b}")
            else:
                print ("error: division by zero is not allowed.")
        else:
                print ("invalid choice . please try again.")
    except ValueError:
                print ("invalid input . please enter numeric values.")
                
    #check if user wants to continue
    ch = input ("\nDo you want to continue? (yes/no): ")
    print()
        
    print ("thank you for using the calculator app!")
        