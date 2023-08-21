import time
import threading

def timeout(seconds):
    def decorator(func):
        def wrapper(*args, **kwargs):
            def target():
                func(*args, **kwargs)
                event.set()

            event = threading.Event()
            thread = threading.Thread(target=target)

            thread.start()
            event.wait(seconds)

            if event.is_set():
                print(f"方法执行正常结束")
            else:
                print(f"方法执行超时，强制退出")
                thread.join()

        return wrapper
    return decorator

@timeout(5)  # 设置超时时间为 5 秒
def my_method():
    while True:
        # 在这里编写死循环的逻辑
        pass

# 调用被装饰的方法
my_method()