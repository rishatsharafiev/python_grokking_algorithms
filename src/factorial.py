def factorial(x):
    """Get factorial of x"""
    try:
        x = int(x)

        if x == 1:
            return 1
        return x * factorial(x - 1)
    except ValueError:
        return None


assert factorial(3) == 1 * 2 * 3
assert factorial(5) == 1 * 2 * 3 * 4 * 5
assert factorial('test') is None
