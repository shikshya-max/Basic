num=int(input("Enter any number:"))
rev=0
temp=num
while(num>0):
    
    mod=num%10
    rev=rev*10+mod
    num=num//10

if (rev==temp):
    print(temp,"is palindrome.")

else:
    print(temp,"isn't palindrome number.")
    

    
