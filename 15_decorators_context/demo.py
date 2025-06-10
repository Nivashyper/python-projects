import time
from contextlib import contextmanager

def timed(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        try:
            return func(*args, **kwargs)
        finally:
            print(f"{func.__name__} took {time.time() - start:.4f}s")
    return wrapper

@contextmanager
def file_writer(path):
    f = open(path, "w", encoding="utf-8")
    try:
        yield f
    finally:
        f.close()

@timed
def compute():
    total = sum(range(1_000_00))
    return total

if __name__ == "__main__":
    print(compute())
    with file_writer("hello.txt") as out:
        out.write("hello")
