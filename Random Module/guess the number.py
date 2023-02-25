import random
n1=int(input("ENTER YOUR NUMBER 1 = "))
n2=int(input("ENTER YOUR NUMBER 2 = "))
a=random.randint(n1,n2)
print("your random no is = ",a)
test=0
while(1>0):
    f= int(input("ENTER YOUR GUESS NUMBER = "))
    if(a==f):
        print("you tack attement = ",test)
        break
    test+=1
if(test<2):
    print("You got a 1st Price")
elif(test>2 and test<5):
    print("You got a 2nd Price")
elif(test>5 and test<10):
    print("You got a 3nd Price")
elif(test>10):
    print("Sorry bad luck try next time")



