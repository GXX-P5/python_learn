"""
input the age of a person in numbers
check if the age is 18 and qualify for driving and if not disqualify them also check if the age is exact 18
and call them physically to apper there
"""

print("enter your age")
age=int(input())


if age > 100:
    print("sorry we dont have no rules for aliens ")
elif age > 18:
    print("you are qualified for driving")
elif age < 5:
    print("stay in school kid")
elif age==18:
    print("you have to appear physically")
else:
    print("your age doesnt match the limit")