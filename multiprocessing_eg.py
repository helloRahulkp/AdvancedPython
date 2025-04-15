import multiprocessing
import time

results_sq = []
results_cu = []

def calc_square(numbers):
    global results_sq
    print("Calculating squares...")
    for i in numbers:
        print("Square:", i * i)
        results_sq.append(i * i)
    print("Squares calculated within process:", results_sq)

def calc_cube(numbers):
    global results_cu
    print("Calculating cubes...")
    for i in numbers:
        print("Cube:", i * i * i)
        results_cu.append(i * i * i)
    print("Cubes calculated within process:", results_cu)

if __name__ == "__main__":
    arr = [2,3,4,5,6]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Squares:", results_sq)
    print("Cubes:", results_cu)

    print("Done!")