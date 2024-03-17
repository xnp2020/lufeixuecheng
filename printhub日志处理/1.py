import os
import multiprocessing
from multiprocessing import Process


def write_file(l, file_path):
    l.acquire()
    try:
        with open(file_path, 'a') as f:
            f.write(str(os.getpid()) + '_' + str(id(l)))
            f.write('\n')
    finally:
        l.release()


if __name__ == '__main__':
    l = multiprocessing.Lock()
    for num in range(10):
        Process(target=write_file, args=(l, './file.txt')).start()
