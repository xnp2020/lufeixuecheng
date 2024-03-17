import multiprocessing
import os
import time
import random
# 设置回调函数


def setcallback(x):
    with open('result.txt', 'a+') as f:

        line = str(x) + "\n"
        f.write(line)


def multiplication(num):
    time.sleep(random.randint(1, 5))
    return f'{os.getpid()}: {num*(num+1)}'


if __name__ == '__main__':
    pool = multiprocessing.Pool(2)
    for i in range(100000000000000000):
        pool.apply_async(func=multiplication, args=(i,), callback=setcallback)
    pool.close()
    pool.join()
