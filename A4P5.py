from math import factorial


def factorial_test(a):
    n=1
    while True:
        if a/factorial(n)==int(a/factorial(n)):
            n=n+1
        elif factorial(n)==a*n:
            print("The number is factorial")
            print(a ,"=",n-1,"!")
            break
        elif factorial(n)!=a*n:
            print("The number is not factorial !!!!!!!")
            break
    
           
a=int(input("Please enter and integer number: "))
factorial_test(a)

