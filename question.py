a="hello world"
print(a)


1
a=int(input("no. "))
if a%2==0:
   print("even")
else:
    print("odd")

2
year=int(input("year?"))
if year %4==0 and year%100!=0:

    print("leap year")
elif year %100==0 and year%400==0:
    print("leap year")
else:
    print("not a leap year")

#3

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
