print(""" 
1.Add
2.Subtract
3.Multiply
4.Divide
""")

ch = int(input("Enter choice (1/2/3/4): "))
if ch in (1, 2, 3, 4):
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))


if ch==1:
    print ("addition :",num1+num2)
elif ch==2:
    print ("subtraction :",num1-num2)
elif ch == 3:
    print("multiplication :", num1 * num2)
elif ch==4:
    print ("divition :",num1/num2)

else:
    print("invalid number")