import threading


g_num = 0


def test1(num):
    global g_num
    for i in range(num):
        g_num += 1


def test2(num):
    global g_num
    for i in range(num):
        g_num += 1

def main():
    t1 = threading.


if __name__ == '__main__':
    main()
