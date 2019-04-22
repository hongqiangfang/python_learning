import gevent
import time
from gevent import monkey

monkey.patch_all()


def f():
    for i in range(10):
        print(gevent.getcurrent(),i)
        time.sleep(0.1)


g1 = gevent.spawn(f)
g2 = gevent.spawn(f)
g3 = gevent.spawn(f)
g1.join()
g2.join()
g3.join()