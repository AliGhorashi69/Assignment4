

def second_order(a,b,c):
    from math import sqrt
    print("The equation is that: ", a,"*x^2  +", b,"*x  +", c)
    if b*2-4*a*c<0:
        print("No Real Number Root!!!")
    else:
        x1=sqrt((b*2-4*a*c))-b/(2*a)
        x2=-sqrt((b*2-4*a*c))-b/(2*a)
        return [x1,x2]

a=float(input("a: "))
b=float(input("b: "))
c=float(input("c: "))

z=second_order(a,b,c)
print(z)