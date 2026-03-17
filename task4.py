import asyncio


async def slow_task() -> None:
    """
    Simulates a long-running task that takes 10 seconds to complete.
    Returns:
        None
    """
    print("Starting long operation")
    await asyncio.sleep(10)
    print("Operation finished successfully")


async def main() -> None:
    """
    Executes the slow task with a defined timeout.
    """
    timeout_seconds = 5

    print(f"Main: Starting slow task with a {timeout_seconds}s timeout.")

    try:
        await asyncio.wait_for(slow_task(), timeout=timeout_seconds)
        print(f"Task completed within the time limit ({timeout_seconds})")

    except asyncio.TimeoutError:
        print(f"Timeout. The task took too long and was cancelled after {timeout_seconds}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    asyncio.run(main())
