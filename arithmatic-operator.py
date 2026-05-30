while True:
    a=int(input("Enter a value :"))
    b=int(input("Enter b value :"))
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulodivision\n5.Floatdivision\n6.Exit...")
    choice=input("Enter your choice :")

    if choice=="1":
        print("Additiion is :",a+b)
    if choice=="2":
        print("Subtraction is :",a-b)    
    if choice=="3":
        print("Multiplication is :",a*b)    
    if choice=="4":
        print("Division is :",a/b)    
    if choice=="5":
        print("Modulodivision is :",a%b)    
    if choice=="6":
        print("Ok...") 
        break 
    else:
        print("wrong choice please enter correct option....")      
