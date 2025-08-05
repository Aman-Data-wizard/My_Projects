#map function
numbers = [2,3,4,5]
def sq(x):
     y = x*x
     return y
l2 = map(sq,numbers)
print(list(l2))