num=int(input("Enter a four digit number"))
temp=num
i=0
rev=0
while temp!=0:
    new=temp%10
    print(f"face value={new}")
    rev=(rev*10)+new
    new=new*(10**i)
    i+=1
    temp=int(temp/10)
    print(f"place value={new}")
    print(f"Reverse of number: {rev}")

