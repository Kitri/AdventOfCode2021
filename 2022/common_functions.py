import time
def run_with_timeprints(func: callable, func_description = ''):
    print(f"---- Start: {func_description}")
    start_time = time.time()
    res = func()
    end_time = time.time()

    print(f"Time taken: {(end_time - start_time)*1000} ms")

    return res