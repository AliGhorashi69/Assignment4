
n=int(input("n: "))
m=int(input("m: "))


def Multiplying_Table(n,m):

  for j in range (1,m+1):
    
        for i in range(1,n+1):
            if i!=n:
                print("    ",i*j,"    ", end="  ")
            
            else: 
                print("    ", i*j,"    ")
           
            
        

Multiplying_Table(n,m)
 
       
