import time
import asyncio
import threading
import multiprocessing
from typing import List, Any

REQ_NUM: int = 500
DELAY: float = 0.1


def sync_task() -> None:
    """
    Performs a synchronous sleep task.
    """
    time.sleep(DELAY)


def run_sync() -> None:
    """
    Executes tasks sequentially in the main thread.
    """
    start: float = time.time()
    for _ in range(REQ_NUM):
        sync_task()
    print(f"Sync: {round(time.time() - start, 2)} сек")


def thread_task() -> None:
    """
    Performs a sleep task intended for execution in a thread.
    """
    time.sleep(DELAY)


def run_threading() -> None:
    """
    Executes tasks concurrently using multiple threads.
    """
    start: float = time.time()
    threads: List[threading.Thread] = []
    for _ in range(REQ_NUM):
        t: threading.Thread = threading.Thread(target=thread_task)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print(f"Threading: {round(time.time() - start, 2)} сек")


def process_task(_: Any) -> None:
    """
    Performs a sleep task in a separate process.
    Args:
        _: Placeholder argument for pool.map.
    """
    time.sleep(DELAY)


def run_multiprocessing() -> None:
    """
    Executes tasks in parallel using a process pool.
    """
    start: float = time.time()
    with multiprocessing.Pool() as pool:
        pool.map(process_task, range(REQ_NUM))
    print(f"Multiprocessing: {round(time.time() - start, 2)} сек")


async def async_task() -> None:
    """
    Performs an asynchronous sleep task.
    """
    await asyncio.sleep(DELAY)


async def run_async() -> None:
    """
    Executes tasks concurrently using an event loop.
    """
    start: float = time.time()
    tasks: List[Any] = [async_task() for _ in range(REQ_NUM)]
    await asyncio.gather(*tasks)
    end_time: float = time.time()
    print(f"Asyncio: {round(end_time - start, 2)} сек")


if __name__ == "__main__":
    run_sync()
    run_threading()
    run_multiprocessing()
    asyncio.run(run_async())
