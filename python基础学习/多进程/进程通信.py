import multiprocessing


def download(q):
    # data=[1,2,3,4,5,6,7]
    for i in range(1000):
        q.put(i)


def analysis(q):
    for i in range(1000):
        pass
    while True:
        a = q.get()
        print(a)
        if q.empty():
            break


def main():
    q = multiprocessing.Queue(1000)
    p1 = multiprocessing.Process(target=download, args=(q,))
    p2 = multiprocessing.Process(target=analysis, args=(q,))
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()
