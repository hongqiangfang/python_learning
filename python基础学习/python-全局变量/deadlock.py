import threading
import time


mutex1 = threading.Lock()
mutex2 = threading.Lock()


# 死锁
class Mythread1(threading.Thread):
    def run(self):
        mutex1.acquire()
        time.sleep(1)
        mutex2.acquire()
        mutex2.release()
        mutex1.release()


class Mythread2(threading.Thread):
    def run(self):
        mutex2.acquire()
        time.sleep(1)
        mutex1.acquire()
        print(2)
        mutex1.release()
        mutex2.release()


def main():
    a = Mythread1()
    b = Mythread2()
    a.start()
    b.start()
    print(1)

if __name__ == '__main__':
    main()
