#محاسبه ب م م


def GCF_Manual(a,b):
    x=1
    if a>b or a==b:
        for i in range (1,b+1):
            if a/i==int(a/i) and b/i==int(b/i):
                x=i
    elif b>a:
         for i in range (1,a+1):
            if a/i==int(a/i) and b/i==int(b/i):
                x=i
    return x


a=int(input("enter an integer value (a): "))
b=int(input("enter an integer value (b): "))
y=GCF_Manual(a,b)
print("The Greatest Commong Factor (GCF) is:", y)