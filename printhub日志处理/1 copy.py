import multiprocessing

# 设置回调函数


def setcallback(x):
    with open('result.txt', 'a+') as f:
        line = str(x) + "\n"
        f.write(line)


def multiplication(num):
    return num*(num+1)


if __name__ == '__main__':
    pool = multiprocessing.Pool(6)
    for i in range(1000):
        pool.apply_async(func=multiplication, args=(i,), callback=setcallback)
    pool.close()
    pool.join()
