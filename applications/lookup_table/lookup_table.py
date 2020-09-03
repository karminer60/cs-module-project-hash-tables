# Your code here


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    cache = {}
​
    def slowfun_too_slow(x, y):
	    if n <= 1:
		    return n
​
	    if n not in cache:
		    cache[n] = fib(n-1) + fib(n-2)
​
	        return cache[n]
​
    for i in range(1000000):
	    print(f"{i}: {fib(i)}")



# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
