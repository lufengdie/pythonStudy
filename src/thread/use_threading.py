import threading, time

# 新线程执行的代码
def loop():
    print('thread %s is running ...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s end.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='CustomLoopThread')
t.start()
t.join()
print('thread %s done.' % threading.current_thread().name)