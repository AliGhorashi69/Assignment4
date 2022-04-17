# محاسبه ک م م 


def LCM_Manual(a,b):
    x=a*b
    if a>b or a==b:
        for i in range (a,a*b+1):
            if i/a==int(i/a) and i/b==int(i/b):
                x=i
    elif b>a:
         for i in range (b,a*a+1):
            if i/a==int(i/a) and i/b==int(i/b):
                x=i
    return x


a=int(input("enter an integer value (a): "))
b=int(input("enter an integer value (b): "))
y=LCM_Manual(a,b)
print("The Least Commong Multiplies (LCM) is:", y)