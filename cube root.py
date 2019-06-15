num=int(input("Enter any number: "))
i=2
c=1


while (i<num):
    
    if (int(round(num**(1/3)))==i):
        print(i,"is the cube root of.", num)
        c=1
        break
        
    else:
        i=i+1
        c=0
if c==0:
    print(num,"is not the perfect cube number.")
    
