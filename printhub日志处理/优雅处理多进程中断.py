# gpt3.5编写
import signal
import multiprocessing
import time
import sys


def worker():
    print("Worker started")
    while True:
        time.sleep(1)


def signal_handler(signum, frame):
    print(f"Received signal {signum}, stopping all processes")
    pool.terminate()
    pool.join()  # 等待所有子进程结束
    print("All processes completed")
    sys.exit(0)  # 使主进程也能够正常退出


def init_process():
    signal.signal(signal.SIGINT, signal_handler)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)

    pool = multiprocessing.Pool(6, initializer=init_process)
    for i in range(6):
        pool.apply_async(func=worker)

    pool.close()

    print("All processes started")

    while True:
        pass  # 等待信号或其他事件发生


# 网上解决方法 https://www.volcengine.com/theme/4204563-R-7-1

# import signal
# import multiprocessing
# import time

# def worker():
#     print("Worker started")
#     while True:
#         time.sleep(1)

# def signal_handler(signum, frame):
#     print(f"Received signal {signum}, stopping all processes")
#     for process in multiprocessing.active_children():
#         process.terminate()

# if __name__ == '__main__':
#     signal.signal(signal.SIGINT, signal_handler)

#     processes = []
#     for i in range(4):
#         p = multiprocessing.Process(target=worker)
#         processes.append(p)
#         p.start()

#     for process in processes:
#         process.join()

#     print("All processes finished")
