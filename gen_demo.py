num=(x*x for x in range(100))
print(num)
print(next(num))
print(next(num))
print(next(num))
print(next(num))
def demo():
    yeild = 'A'
    yeild = 'B'
    yeild = 'C'
x=demo()
for i in x:
    print(i)