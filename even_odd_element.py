#Python program to find total number of odd and even numbers.
list=[1,3,4,6,8,9,11,13,14,16]
even=0
odd=0
for i in list:
    if(i%2==0):
        even=even+1
    else:
        odd=odd+1
print("even number", even)
print("odd number",odd)            