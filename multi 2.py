from multiprocessing import Pool
import time

def squared(n):
    time.sleep(1)
    return n * n

if __name__ == "__main__":
    # map parallel
    numbers = [1, 2, 3, 4, 5]

    with Pool(processes=3) as pool:
        result = pool.map(squared, numbers)

    print(result)