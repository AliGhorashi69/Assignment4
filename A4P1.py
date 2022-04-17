n=int(input("Enter width"))
m=int(input("Enter Length"))

def chess(n,m):

  for j in range (m):
    
    if (j/2)==int(j/2):
        for i in range(n):

            if (i/2)==int(i/2) and i!=n-1:
                print("#", end="")
                
            elif (i/2)!=int(i/2) and i!=n-1:
                print("*", end="")
                
            elif (i/2)==int(i/2) and i==n-1:
                print("#")
                
            elif (i/2)!=int(i/2) and i==n-1:
                print("*")
    else:
        for i in range(n):

            if (i/2)==int(i/2) and i!=n-1:
                print("*", end="")
                
            elif (i/2)!=int(i/2) and i!=n-1:
                print("#", end="")
                
            elif (i/2)==int(i/2) and i==n-1:
                print("*")
                
            elif (i/2)!=int(i/2) and i==n-1:
                print("#")
            
        

chess(n,m)