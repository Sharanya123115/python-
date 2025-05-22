#s={}
#print(type(s))

#s={1,12,33,}
#print(type(s))

#s={2,42,5,25,2,5,2,55}
#print(s)#duplicates are not allowed

#s={2,42,5,25,2,5,2,55,1,0,4}
#print(s)

'''
#set methods
add
update
pop
remove
'''
#s={2,42,5,25,2,5,2,55,1,0,4}
#s.add(123)
#s.update({1,2,4,35,5})
#s.pop()
#s.remove(42)
#print(s)

'''
set operations
union
intersection
difference
issubset
issuperset
'''
#set1={1,2,3}
#set2={4,5,6}
#print(set1.union(set2))

#s1={1,2,3,4}
#s2={4,5,6}
#print(s1.intersection(s2))

#s1={1,2,3,4}
#s2={4,5,6}
#print(s1.difference(s2))

#s1={1,2,3,4,5,6}
#s2={4,5,6}
#print(s1.issuperset(s2))

s1={1,2,3,4,5,6}
s2={4,5,6}
print(s2.issubset(s1))
