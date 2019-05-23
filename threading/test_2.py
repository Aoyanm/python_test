from threading import Thread
from queue import Queue

#继成Thread库下的Thread类
class myThread(Thread):
    def __init__(self):
        Thread.__init__(self)#开启Thread库下__init__到本类中
    def main(self):
        print("test")
    def run(self):
        while not  q.empty():
            # print(q.get())#取24行循环添加到q.put里的数据
            print("True")
        else:
            print("False")

        self.main()


if __name__ == '__main__':
    q = Queue()
    th = []
    for i in range(5):
        q.put(i)
    myThread().start()