#namedtuple
from collections import namedtuple

a = namedtuple("courses", "name, technology")
s = a._make(["Artificial intelligence", "Python"])

print(s)

#deque
from collections import deque

b = ["e", "d", "u", "r", "e", "k", "a"]
d = deque(b)
print(d)

#d.append("Python")
#print(d)

d.appendleft("Python")
print(d)
d.pop()
print(d)

d.popleft()
print(d)

#chainmap
from collections import ChainMap

c = {1:"edureka", 2:"Python"}
e = {3:"ML", 4:"AI"}

c1 = ChainMap(c, e)
print(c1)

#counter
from collections import Counter

ct = [1, 1, 2, 3, 2, 2, 4, 5, 4, 5, 4, 3, 6, 2, 2, ]
ctr = Counter(ct)
print(ctr)
print(list(ctr.elements()))
print(ctr.most_common())
sub = {2:1, 6:1}
print(ctr.subtract(sub))
print(ctr.most_common())

#OrderedDict
from collections import OrderedDict

dic = OrderedDict()
dic[1] = "e"
dic[2] = "d"
dic[3] = "u"
dic[4] = "r"
dic[5] = "e"
dic[6] = "k"
dic[7] = "a"

print(dic)
print(dic.keys())
print(dic.items())

#defaultdict
from collections import defaultdict

dfd = defaultdict(int)
dfd[1] = "Python"
dfd[2] = "edureka"

print(dfd[3])

f = {1:"Python", 2:"Edureka"}
print(f[3])

#UserDict, UserList, UserString












