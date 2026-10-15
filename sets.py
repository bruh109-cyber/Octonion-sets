from NumberSets import Octonion

c = Octonion(1, 2, 3, 4, 5, 6, 7, 8)
d = Octonion(4, 5, 9, 4, 5, 6, 7, 8)
a = Octonion(4, 5, 9, 4, 5, 9, 5, 4)
print(a*(c*d))
print(d*(c*a))







