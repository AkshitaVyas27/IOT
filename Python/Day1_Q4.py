

def max(num1:int,num2:int,num3:int):
    if num1>num2:
        if num1>num3:
            return num1
    else:
        if num2>num3:
            return num2
        else:
            return num3
        
num1=int(input("ENter num1 "))
num2=int(input("Enter num2 "))
num3=int(input("Enter num3 "))

maxi=max(num1,num2,num3)
print(f"Max of three numbers is {maxi}")
            
        
