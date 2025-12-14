def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if(b==0):
        return "Division is not possible with zero"
    else:
        return a/b

def calculator():
    while True:
        print("Select operation:")
        print("1.Add")
        print('2.Subtraction')
        print("3.Multiplication")
        print("4.Division")
        print("5.Exit")

        c=input("Enter your choice:")
        if(c=='5'):
            print("Exiting....")
            break
        a=float(input("Enter the first number: "))
        b=float(input("Enter the second number: "))
        if(c=='1'):
            print("Sum is: ",add(a,b))
        elif(c=='2'):
            print("Difference is: ",sub(a,b))
        elif(c=='3'):
            print("Product is: ",mul(a,b))
        elif(c=='4'):
            print("Quotient is: ",div(a,b))
        else:
            print("Invalid input")
        
calculator()
