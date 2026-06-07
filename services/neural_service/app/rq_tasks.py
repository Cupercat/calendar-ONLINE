from redis import Redis
from rq import Queue
from app.gigachat_client import call_gigachat
import os

redis_conn = Redis(host=os.getenv("REDIS_HOST", "redis"))
q = Queue(connection=redis_conn)

def process_ai_request(prompt: str):
    result = call_gigachat(prompt)
    # можно сохранить результат в MongoDB
    return result