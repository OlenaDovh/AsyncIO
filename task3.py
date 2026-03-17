import asyncio


async def producer(queue: asyncio.Queue) -> None:
    """
    Produces tasks and adds them to the queue with a delay.
    Args:
        queue (asyncio.Queue): The queue to add tasks to.
    Returns:
        None
    """
    for i in range(1, 6):
        await asyncio.sleep(1)
        task_name = f"Task-{i}"
        await queue.put(task_name)
        print(f"[Producer] Added {task_name} to the queue.")

    print("[Producer] Finished adding tasks.")


async def consumer(queue: asyncio.Queue, num: int) -> None:
    """
    Consumes tasks from the queue and processes them.
    Args:
        num (int): Identifier for the consumer instance.
        queue (asyncio.Queue): The queue to get tasks from.
    Returns:
        None
    """
    while True:
        task = await queue.get()

        if task is None:
            print(f"[Consumer {num}] Завершення роботи")
            queue.task_done()
            break

        print(f"[Consumer {num}] Started processing {task}")
        await asyncio.sleep(2)
        print(f"[Consumer {num}] Finished {task}")

        queue.task_done()


async def main() -> None:
    """
    Initializes the queue and manages producers and consumers.
    """
    queue = asyncio.Queue()
    producer_task = asyncio.create_task(producer(queue))

    consumers = [
        asyncio.create_task(consumer(queue, i))
        for i in range(1, 4)
    ]

    await producer_task
    await queue.join()

    for c in consumers:
        c.cancel()

    print("All tasks are processed successfully.")


if __name__ == "__main__":
    asyncio.run(main())
