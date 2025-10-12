x = int(input("Enter a number greater than one: "))
y=int(x/2)
i=1
c=0
while i<y:
    i+=1
    if(x%i==0):
        c+=1
if(c==0):
    print("your number is prime")
else:
    print("your number is not prime")

