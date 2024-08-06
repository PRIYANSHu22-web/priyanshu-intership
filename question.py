1
a="hello world"
print(a)

2
name,age="priyanshu", 22
favoritehobby="reading books"
print("name: {} \nage: {} \nfavoritehobby:{}".format(name,age,favoritehobby)) 

3
comment="my code explain about my skills  "
print(comment)

4
n=float(input("number="))
if n>0:
    print("positive")
elif n==0:
    print("zero")
else: 
 print("negative")

5
year=int(input("year?"))
if year %4==0 and year%100!=0:

    print("leap year")
elif year %100==0 and year%400==0:
    print("leap year")
else:
    print("not a leap year")

6
n=int(input("no. ?"))
for i in range(1,n+1):
    print(i)

7
multiplier=int(input("number "))
counter=1
while counter<=10:
    result=counter*multiplier
    print(f"{counter}*(multiplier)={result}")
    counter += 1
    
8




9
n=0
for i in range(10):
    n+=1
    if n==5:
        break
    print("value",n) 

10
def greet(name):
    print(f"hello,{name}!")

    
#z= input("character")
#if z in "aeiouAEIOU":
 #   print("vowel")
#else:
 #   print("consonent")

#LOOP QUESTIONS
#1

#n=int(input("no. ?"))
#for i in range(1,n+1):
 #   print(i)

#2

#n=int(input("no.?"))
#for i in range(n,0,-1):
 #   print(i)

#3

#n=int(input("table"))
#for i in range(1,11):
 #   print(f"{n} * {i}= {n * i}")

#4

#n=int(input("no.? "))
#sum=0
#for i in range(1,n+1):
 #   sum=sum+i
    
#print(sum)

#5

#factorial of no. strong no. program
#n=int(input("no.?"))
#fact=1
#for i in range(1,n+1):
 #   fact=fact*i

#print(fact)    
            
#6 factor of all no.

#n=int(input("no.?"))
#print("all the factor are" )
#for i in range(1,n+1):
#    if n%i==0:
 #       print(i,end=" ")           

#7 excluding factor

#n=int(input("no.? "))
#sum=0
#for i in range(1,n):
#    if n%i==0:
#        sum=sum+i
#if sum==n:
#    print("strong no.")
#else:
#    print("not a strong no.")         

#8 prime no.

#n=int(input("no.? "))
#count=0
#for i in range(1,n+1):
#    if n%i==0:
#        count=count+1
#if count==2:
#    print("prime no.")
#else:
#    print("composite no.")            

#9
#a=int(input("no.?"))
#while a>0:
#    print(a%10)
#    a=a//10

#10 pallidonmic
#n=int(input("no.? "))
#copy=n
#rev=0
#while n >0:
#    z=n%10
#    rev=rev*10+z
#    n=n//10
#if copy==rev:
#    print("pallindromic no.")

#else:
#    print("no pallindromic ")    

#11
