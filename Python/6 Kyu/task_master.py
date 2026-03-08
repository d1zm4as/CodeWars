from concurrent.futures import *

def task_master(a):
    with ThreadPoolExecutor(max_workers=len(a)) as executor:
        return sum(executor.map(lambda f: f(), a))