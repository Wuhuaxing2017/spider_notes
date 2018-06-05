import threading

# 导入队列
from queue import Queue

# 全局设置一个标志，flag
exitFlag = False

import time


class MyThread(threading.Thread):

    def __init__(self, queue,ijfsfsjfasfj):
        super().__init__()
        self.queue = queue
        self.id = ijfsfsjfasfj

    def run(self):
        super().run()
        # 声明成全局的变量
        global exitFlag

        while True:
            if exitFlag:
                break
            #         从queue中获取数据
            #     block 阻塞，True 当队列中没有数据的时候，就会阻塞
            try:
                data = queue.get(block=False)
                time.sleep(1)
                print('线程------%d-------执行任务：从队列中获取的数据是：%d' % (self.id,data))
                #     告诉队列任务完成
                queue.task_done()
            except Exception as e:
                # print('队列为空，无法从队列中获取数据')
                pass
    # 重写Thread的方法，自定义，
    # Ctrl + O

if __name__ == '__main__':

    # 队列，类比成列表
    queue = Queue()

    for i in range(10):
        queue.put(i)

    # 队列中有10个数据
    # 子线程中，获取queue中的数据
    # 获取数据：get
    for i in range(1, 4):
        th = MyThread(queue,i)
        th.start()

    # 队列中所有的数据必须全部取出来，锁才会消失
    # th.join()
    queue.join()
    exitFlag = True
    # 只要任务完成，现在就修改全局的flag，告诉子线程，break
    # global exitFlag

    # 去线程中，获取数据并且进行打印出来
    # print(queue.get(block=False))
