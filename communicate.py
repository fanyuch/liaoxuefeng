from multiprocessing import Process, Queue
import os, time, random

def write(my_queue):
    print('process to write %s' %os.getpid())
    for value in ['a', 'b', 'c']:
        print('put %s to queue...'%value)
        my_queue.put(value)
        time.sleep(random.random())


def read(my_queue):
    print('process to read %s' %os.getpid())
    while True:
        value = my_queue.get(True)
        print('get %s from queue'%value)

if __name__ == '__main__':
    q = Queue()
    pWrite = Process(target=write, args=(q,))
    pRead = Process(target=read, args=(q,))

    pWrite.start()
    pRead.start()

    pWrite.join()
    pRead.terminate()

balance = 0
import threading
lock = threading.Lock()

def run_thread(n):
    for i in range(10000):
        lock.acquire()
        try:
            n += 1
        finally:
            lock.release()


# import queue
# from multiprocessing.managers import BaseManager
#
# task_queue = queue.Queue()
# result_queue = queue.Queue()
#
# class QueueManager(BaseManager):
#     pass
#
# QueueManager.register('get_task_queue', callable=lambda:task_queue)
# QueueManager.register('get_result_queue', callable=lambda:result_queue)
#
# manager = QueueManager(address=('', 5000),authkey =b'abc')
# manager.start()
#
# task = manager.get_task_queue()
# result = manager.get_resut_queue()
#
# for i in range(10):
#     n = random.randint(0, 10000)
#     print('put task %d'%n)
#     task.put(n)
#
# print('try get results...')
# for i in range(10):
#     r = result.get(timeout = 10)
#     print('result: %s'%r)
#
# manager.shutdown()
# print('master exit')

