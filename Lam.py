#lambda function
#lambda arguments: expression
sq = lambda x: x*x
print(sq(5))

#greater among numbers
greater = lambda x, y: "x is greater than y" if x > y else "y is greater than x"
print(greater(5, 3))


def make_incrment(n):
     return lambda x: x+n
f = make_incrment(50)

print(f(1))