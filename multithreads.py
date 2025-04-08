import time
import threading

def sq(numbers):
    print("Calculating squares...")
    for n in numbers:
        time.sleep(0.5)
        print(f"Square of {n}: {n * n}")
    print("Squares calculated.")
def cube(numbers):
    print("Calculating cubes...")
    for n in numbers:
        time.sleep(0.5)
        print(f"Cube of {n}: {n * n * n}")
    print("Cubes calculated.")

t=time.time()
arr = [2,3,8,9]

sq(arr)
cube(arr)
print("Total time taken without threading:",time.time()-t)
print("Using threading...")
t=time.time()
t1 = threading.Thread(target=sq, args=(arr,))
t2 = threading.Thread(target=cube, args=(arr,))
t1.start()
t2.start()
t1.join()
t2.join()
print("Total time taken with threading:",time.time()-t)