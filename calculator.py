while True:
    choice = input(" what operation you want to do (+,-,*,/)=")

    n1=int(input("enter 1st number=")) 
    n2=int(input("enter 2nd number="))
    if choice == "+":
        print("sum=",n1+n2)
    elif choice == "-":
        print("sub=",n1-n2)
    elif choice == "*":
        print("product=",n1*n2)
    elif choice == "/":
        if n2==0:
            print(" not divisible by zero")
        else:  
            print("divide=",n1//n2)
    ch=input("do you want to use again( y or n)=")
    if ch.lower() !="y":
        print("thankyou")
        break
