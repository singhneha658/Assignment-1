#Python program to reverse the string taken from the user as an input.
str=input("Enter a word to reverse it:  ") 
for i in range((len(str)-1),-1,-1):
     print(str[i],end="")