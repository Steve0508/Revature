s1='hello world'

s2=lambda func:func.upper()
print (s2(s1))



#if elif else

n=lambda x:"Positive " if x>0 else "Negative" if x<0 else "zero"

print (n(5))
print(n(-3))
print(n(0))



sq=lambda x:x ** 3  #single line

print(sq(3))