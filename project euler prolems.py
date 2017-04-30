# Problem 1 
a=[]
for i in range(1000):
    if((i%3==0) or (i%5==0)):
        a.append(i)
print (a)
print(sum(a))

# Problem 2 
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

# Problem 3 
def prime_factor(num):
    curr_num = num
    a = 2
    factors = []
    while a <= num:
        while num%a == 0:
            num = num /  a
            factors.append(a)
        a = a + 1
    print('The largest prime factor of given number ' + str(curr_num) + ' are = ' +  str(factors))

prime_factor(600851475143)
