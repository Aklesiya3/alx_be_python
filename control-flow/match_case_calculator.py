num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))
operation = input("choose the operation (+ , - , * , /): ")
match operation:
    case "+" :
        print("the result is " , num1+num2 )
    case "-":
        print ("the result is" ,num1 - num2 )
    case "*":
        print("the result is " , num1 * num2 )
    case "/":
        if num2 != 0:
            print(" the result is " , num1 / num2) 
        else:
            print("cannot divide by zero")
    case _ :
        print(" you enter invalid operation")
