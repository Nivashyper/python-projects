import time, threading

class Task(threading.Thread):
    def __init__(self, name, interval, func):
        super().__init__(daemon=True)
        self.name, self.interval, self.func = name, interval, func

    def run(self):
        while True:
            self.func()
            time.sleep(self.interval)

def say_hello():
    print("Hello every 5s")

if __name__ == "__main__":
    Task("hello", 5, say_hello).start()
    while True:
        time.sleep(1)
