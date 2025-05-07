s = 'Python'

print(s[4], s[:4])
print(s[:4])
print(s[1:4:])
print(s[::-1])

l = [3,7,[1,4,'hello']]
l[2][2] = "goodbye"
print(l)

d1 = {'simple_key':'hello'}
print(d1['simple_key'])
d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])

mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
unique = []
for i in mylist:
    if i not in unique:
        unique.append(i)
print(unique)

age = 4
name = "Sammy"
print(f"Hello my dog's name is {name} and he is {age} years old")


