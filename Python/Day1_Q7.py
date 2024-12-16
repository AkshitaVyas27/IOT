collection=[0,1,2,3,4,5,6,7,8,9,10]



for num in collection:
    fact=1
    temp=num
    while temp!=0:
        fact=fact*temp
        temp-=1
    print(f"factorial of {num} = {fact}")


