import threading

# def main():
#     print(threading.active_count()) #显示有多少个线程
#     print(threading.enumerate())#显示分别是什么线程
#     print(threading.current_thread())#当前运行的线程

def addThre_job():
    print("Yes -1")


def main():
    add_thread = threading.Thread(target=addThre_job())#threading.Thread添加一个线程
    add_thread.start()#开启


if __name__ == '__main__':
    main()