#faulty calculator
#45*3=555,56+9=77,56/6=4
#DESIGN A CALCULATOR WHICH WILL RETURN THE RITGHT VALUES EXPECPT THE ONES WRITTEN ABOVE
#TAKE INPUT OF THE OPERATOR AND THAN TWO NUMBERS AND GIVE CORRECT RESULT

print("please select the operation you want to perform-->")

print("*")
print("/")
print("+")
print("-")

op=input()
print("youve chosen --",op)

v1=int(input("please insert the first value--"))
v2=int(input("please insert the second value--"))

print("your first value is--",v1)
print("your second value is--",v2)

s1=(43*3)
s2=(56+9)
s3=(56/6)

sum=(v1 + v2)
mul=(v1 * v2)
sub=(v1 - v2)
div=(v1 / v2)


if s1:
    print(int("555"))

elif s2:
    print(int("77"))

elif s3:
    print(int("4"))

elif "+":
    print("the total of your value is --",sum)
else:
    print("none")



























"""
if s1:
    print(int("555"))

elif s2:
    print(int("77"))

elif s3:
    print(int("4"))



else:
    print("none")
"""