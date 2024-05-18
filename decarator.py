def repeat(n):
    def decorator(f):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = f(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()
