def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    
    return fibonacci

fibonacci_func = caching_fibonacci()

print(fibonacci_func(10))  # Виведе 55
print(fibonacci_func(15))  # Виведе 610
