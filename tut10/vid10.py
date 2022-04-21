
#dictionary is noting but key word pairs
"""
a1={}
print(type(a1))
"""

"""
a2={"gautam":"water","shu":"soda","bham":"alcohol"}
print(type(a2))
print(a2["gautam"])
"""

a3={"gautam":"water","shu":"soda","bham":"alcohol", "rohan":{"m":"maggie" , "n":"roti sabzi" , "eve":"dinner"}}
a3["ankit"]="junk food"
a3[430]="kebab"
print(a3[430])

del a3[430]
print(a3)
print("now printing the morning breakfast of rohan")
print(a3["rohan"]["m"])
"""
a4=a3           
print(a4)
del a4["gautam"]
print(a3)
"""

"""
print(a3)
a4=a3.copy()
del a3["gautam"]
print(a4)
"""


#a3={"gautam":"water","shu":"soda","bham":"alcohol", "rohan":{"m":"maggie" , "n":"roti sabzi" , "eve":"dinner"}}
#print(a3.get("gautam"))
#a3.update({"leena":"toffee"})
#print(a3)
# print(a3.keys())
#print(a3.items())