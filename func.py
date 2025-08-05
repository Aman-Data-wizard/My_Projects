def fib(n):
     a, b = 0, 1
     while a < n:
          print(a, end=" ")
          a, b = b, a + b
          print()
fib(100)

def n(a, L=[]):
     L.append(a)
     return L
print(n(1))
print(n(2))
print(n(3))

#keyword arguments
def parrot(voltage, state='a stiff', action='voom', type= 'Norwegian Blue'):
     print("-- This parrot wouldn't", action, end=' ')
     print("if you put", voltage, "volts through it.")
     print("-- Lovely plumage, the", type)
     print("-- It's", state, "!")
parrot(1000)
parrot(voltage=1000)                        #keyword arguments
parrot(voltage=1000000, action='VOOOOOM')

def cheeseshop(kind, *arguments, **keywords):
     print("-- do you have any", kind, "?")
     print("-- I'm sorry, we're all out of", kind)
     for arg in arguments:
          print(arg)
     print("-" * 40) #keyword arguments
     
     for kw in keywords:
          print(kw, ":", keywords[kw])
          
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper = "Michael Palin",
           client = "John Cleese",
           sketch = "Cheese Shop Sketch")
