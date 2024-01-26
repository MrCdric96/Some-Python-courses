"""Mathematical set operations:
insertion (AND): set1 & set2
union (OR): set1 | set2
symmetric difference (XOR): set1 ^ set2 difference(in set1 but not set2): set1 - set2
subset(set2 contains set1): set1 <= set2
superset(set1 contains set2): set1 >= set2
"""

s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1 & s2)
print(s1 | s2)
print(s1 ^ s2)
print(s1 - s2)
print(s1 <= s2)
print(s1 >= s2)