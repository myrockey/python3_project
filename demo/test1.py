#!/usr/bin/python3

print("test python3")
a = [ 1,2,3,4,5 ]
print(a[:]) # [1, 2, 3, 4, 5]
print(a[0:]) # [1,2,3,4,5]
print(a[:100]) # [1,2,3,4,5]
print(a[-1:]) # [5]

def f(): pass
print(type(f())) # <class 'NoneType'>

a = [1,2,3,None,(),[],]
print(len(a)) # 6
print(a) # [1, 2, 3, None, (), []]