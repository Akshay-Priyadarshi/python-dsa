import time


def time_elapsed(task_name: str, func, *args, **kwargs):
    print(f"[{task_name}]START")
    start_time = time.perf_counter()  # Record the start time with high resolution
    res = func(*args, **kwargs)  # Execute the function with the given arguments
    end_time = time.perf_counter()  # Record the end time with high resolution
    print(f"[{task_name}]END")
    elapsed_time = end_time - start_time  # Calculate the elapsed time in seconds
    elapsed_time_ms = elapsed_time * 1000  # Convert seconds to milliseconds
    print(f"[{task_name}]TIME ELAPSED(ms): {elapsed_time_ms} ms")
    print(f"[{task_name}]RESULT: {res}")
    return res
