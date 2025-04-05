import time
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken to execute {func.__name__}: {(end - start)*1000} Mili seconds")
        return result
    return wrapper
#without decorators analying function performance with respect to time
def square(numbers):
    start = time.time()
    result = []
    for number in numbers:
        result.append(number * number)
    end = time.time()
    print(f"Time taken to square {number}: {(end - start)*1000} Mili seconds")
    return result
#with decorators analying function performance with respect to time
@time_it
def cube(numbers):
    result = []
    for number in numbers:
        result.append(number * number * number)
    return result
array = range(1, 100000)
out_sq=square(array)
out_cub=cube(array)