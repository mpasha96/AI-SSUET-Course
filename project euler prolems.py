# Problem 1 Multiples of 3 and 5
a=[]
for i in range(1000):
    if((i%3==0) or (i%5==0)):
        a.append(i)
print (a)
print(sum(a))

# Problem 2 Even Fibonacci numbers
a=1
b=2
c = a + b
s=[1,2,3]
for i in range(40):
   a=b
   b=c
   c=a+b
   if c % 2 == 0 and c < 4000000:
    s.append(c)
print(s)
print(sum(s))