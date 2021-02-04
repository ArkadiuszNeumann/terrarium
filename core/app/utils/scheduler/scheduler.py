from threading import Lock
import asyncio
import schedule
from typing import List
import functools


class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class ScheduleTasks(metaclass=SingletonMeta):
    jobs: List = []

    def __init__(self):
        self.active = True

    async def run(self):
        while self.active:
            await asyncio.sleep(1)
            schedule.run_pending()

    def add_job(self, job, hour_minute):
        self.jobs.append(schedule.every().day.at(f":{hour_minute}").do(job))
        return

    def remove_job(self):
        self.jobs.pop()
        schedule.cancel_job(self.jobs[0])
        return

    def add_job_to_db(self):
        pass

    def parse_time(self):
        return schedule.every(5).seconds
