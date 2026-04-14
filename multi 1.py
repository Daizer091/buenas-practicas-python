from multiprocessing import Process

def compute():
    total = sum(i * i for i in range(10_000_000))
    print(total)

if __name__ == "__main__":
    p1 = Process(target=compute)
    p2 = Process(target=compute)

    p1.start()
    p2.start()

    p1.join()
    p2.join()