def get_fib(position):
    if position < 0:
        return 0
    elif position == 1:
        return 1
    elif position == 2:
        return 1
    else:
        return get_fib(position - 1) + get_fib(position - 2)

# Test cases
print(get_fib(9))
print(get_fib(12))
print(get_fib(28))
print(get_fib(38))
