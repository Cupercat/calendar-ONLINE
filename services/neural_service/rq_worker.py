from redis import Redis
from rq import Worker, Queue
import os

redis_conn = Redis(host=os.getenv("REDIS_HOST", "redis"))
q = Queue(connection=redis_conn)
worker = Worker([q], connection=redis_conn)
worker.work()