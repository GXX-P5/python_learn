s=set()
"""
print(type(s))
s_list=set([1,2,3,4,5])
print(type(s_list))
l=s_list
print(type(l))
print(l)
"""

"""s.add(1)
s.add(1)
s.add(2)
print(s)

#s.union({1,2,3,4})
print(s)
s1=s.union({1,2,3,4})
print(s,s1)
s2=s.intersection({1,2,3,4})
print(s,s2)
"""

s=set()

s.add(1)
s.add(2)
s1=set([1,2])
s.remove(2)
print(type(s1))
print(s)

