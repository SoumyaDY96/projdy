# -*- coding: utf-8 -*-
def add(n1,n2):
    return n1 + n2

def subtraction(n1,n2):
    return n1 - n2
    
def multiplication(n1,n2):
    return n1 * n2
    
def division(n1,n2):
    return n1 / n2

def lcm(n1,n2):
    M=n1 if n1>n2 else n2
    while M<=(n1*n2):
        if M%n1==0 and M%n2==0:
            return M
        M+=1

def hcf(n1,n2):
    N=n1 if n1<n2 else n2
    while N>=1:
        if n1%N==0 and n2%N==0:
            return N
        N-=1

def mod(n1,n2):
    return n1%n2  

def exponent(n1,n2):
    return n1**n2      
    
if __name__ == '__main__':
    
    operations = {
        "+" : add,
        "-" : subtraction,
        "*" : multiplication,
        "/" : division,
        "lcm" : lcm,
        "hcf" : hcf,
        "%" : mod,
        "**" : exponent
    }
    
num1 = float(input("What is the first number: "))
mult_op= True

while mult_op:
    
    try:
        num2 = float(input("What is the second number: "))
        if isinstance(num2,float) == False:
            raise ValueError
        for i in operations.keys():
            print(i)
            
        cal = input("What is the operation? : ")
        
        if cal not in operations.keys():
            raise KeyError
        
        print(f"{num1} {cal} {num2}")
        
        result_func=operations[cal]
        
        rs = result_func(num1,num2)
        
        print(rs)
        
        cnt = input("Do you want to continue? 'y' or 'n' :")
    except ValueError:
            print("Not a number")
            continue
    except KeyError:
            print("Not a valid operation")
            continue
    if cnt == 'y':
        mult_op = True
        num1 = rs
    elif cnt == 'n':
        mult_op = False
print("OK! Have a Good Day")        
    
    