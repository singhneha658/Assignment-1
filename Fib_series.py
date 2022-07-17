#Python program to find Fibonacci series upto the given number.
no=50
no1=0
no2=1
if no<=0:
    print("Enter a valid number")
else:
    
    for i in range(0,50):
        sum=no1+no2 
        no1=no2 
        no2=sum   
        print(sum)    