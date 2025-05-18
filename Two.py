# classmates = ['Michael', 'Bob', 'Tracy']
# classmates.insert(1, 'Jack')
# classmates.pop(1)
# print(classmates)
# print(classmates)
# print(len(classmates))
# print(classmates[0])

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

# sth= {'a': 1, 'b': 2, 'c': 3}
# print(sth.get('a',-11))
# sth1={1,2,3,3}
# print(sth1)

# def enroll(name, gender,sth='newBee'):
#     print('name:', name,'6')
#     print('gender:', gender)
#     print('sth:', sth)
#     print('\n')
#
# enroll(2,3)
# enroll(4,5,sth='666')
# enroll(6,7,'66666')

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0])
print(L)
L=L[1:3]
print(L)
#
# a=[x * x for x in range(1, 11)]
# b= [x * x for x in range(1, 11) if x % 2 == 0]
# c=[m + n for m in 'ABC' for n in 'XYZ']
# d=[x if x % 2 == 0 else -x for x in range(1, 11)]
# print(a)
# print(b)
# print(c)
# print(d)

# d = {'x': 'A', 'y': 'B', 'z': 'C' }
# for k,v in d.items():
#     print(k,'=',d[k])
#     #print(k,'=',v)
#
# for k in d.items():
#     print(k)
#     #print(k,'=',v)
#
# for k,v in d.items():
#     print(k,'=',d[k])
#     #print(k,'=',v)

# g = (x * x for x in range(10))
# print(next(g))
# print(next(g))
# print(next(g))
# def b():
#     yield 4
# c=b()
# print(next(c))