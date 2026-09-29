#WRITE THE PYTHON PROGRAM THAT TAKES A POSITIVE INTEGER N AS  
#INPUT FROM THE USER AND IT SHOULD FIND ALL  PAIRS OF POSITIVE INTEGERS X,Y SUCH THAT X CUBE + Y CUBE =N
n = int(input("Enter n: "))
for x in range(1,n):
    for y in range(1,n):
        if x**3 + y**3 == n:
            print(x,y)