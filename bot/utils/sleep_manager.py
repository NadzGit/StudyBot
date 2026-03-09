import asyncio

def make_sleep():
    async def sleep(delay, result=None):
        coro = asyncio.sleep(delay, result=result)
        task = asyncio.create_task(coro)
        sleep.tasks.add(task)
        try:
            return await task
        except asyncio.CancelledError:
            raise
        finally:
            sleep.tasks.remove(task)

    sleep.tasks = set()
    sleep.cancel_all = lambda: [task.cancel() for task in list(sleep.tasks)]
    return sleep

sleep = make_sleep()