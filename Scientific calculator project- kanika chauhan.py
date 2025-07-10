import math
while True: #This loop will run again and again until we break it
   print("Scientific Calculator in Python")
   print("Choose an Operator:")
   print("1.Add")
   print("2.Subtract")
   print("3.Multiply")
   print("4.Divide")
   print("5.Square root")
   print("6.Power(x^y)")
   print("7.Sine")
   print("8.Cosine")
   print("9.Tangent")
   print("10.Log")
   print("11.Exit")
   #Take user choice
   choice=input("Enter the choice(1 to 11):")
   #Perform action based on choice
   if choice=="1":
        a=float(input("Enter first number:"))
        b=float(input("Enter second number:"))
        print("Answer:",a+b)
   elif choice=="2":
        a=float(input("Enter first number:"))
        b=float(input("Enter second number:"))
        print("Answer:",a-b)
   elif choice=="3":
        a=float(input("Enter first number:"))
        b=float(input("Enter second number:"))
        print("Answer:",a*b)
   elif choice=="4":
        a=float(input("Enter first number:"))
        b=float(input("Enter second number:"))
        if b==0:
             print("Can't divide by 0")
        else:
           print("Answer:",a/b)
   elif choice=="5":
        a=float(input("Enter number:"))
        print("Square root:",math.sqrt(a))
   elif choice=="6":
        a=float(input("Enter base:"))
        b=float(input("Enter power:"))
        print("Answer:",math.pow(a,b))
   elif choice=="7":
        angle=float(input("Enter angle in degrees:"))
        print("Sine:",math.cos(math.radians(angle)))
   elif choice=="8":
        a=float(input("Enter angle in degrees:"))
        print("Cosine:",math.cos(math.radians(angle)))
   elif choice=="9":
        angle=float(input("Enter angle in degrees:"))
        print("Tangent:",math.tan(math.radians(angle)))
   elif choice=="10":
        a=float(input("Enter number:"))
        if a<=0:
            print("Log not defined for 0 or negative numbers")
        else:
            print("Log(base 10):",math.log10(a))
   elif choice=="11":
        print("Thanku for using the calculator Goodbye!")
        break     #this stops the loop and exits the program         
   else:
       print("Invalid choice.Please try again")
                              


    





    









    


