num1=int(input("Enter sub1:"))
num2=int(input("Enter sub2:"))
num3=int(input("Enter sub3"))

avg=(num1+num2+num3)/3
if avg>=90 and avg<=100:
    print("Grade A")
elif avg>=80 and avg<=89:
    print("Grade B")
elif avg>=70 and avg<=79:
    print("Grade C")
elif avg>=60 and avg<=69:
    print("Grade D")
elif avg>=0 and avg<=59:
    print("Grade F")
else:
    print("Invalid number")