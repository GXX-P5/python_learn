dic={"gautam":"water","rohan":"pav bhaji","b":"milk"}
print(type(dic))
print(dic.keys())


print("the key list is as follows-->")
print("gautam")
print("rohan")
print("b")
usr=input("enter one key from the following list")

if usr=="rohan":
    print(dic["rohan"])
elif usr=="gautam":
    print("dic[gautam]")
else:
    print(dic["b"])
