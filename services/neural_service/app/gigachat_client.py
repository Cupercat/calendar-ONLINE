import os
from gigachat import GigaChat

def call_gigachat(prompt: str) -> str:
    # ai-tunnel: можно добавить прокси через переменную окружения
    giga = GigaChat(credentials=os.getenv("GIGACHAT_AUTH_KEY"))
    response = giga.chat(prompt)
    return response.choices[0].message.content