# from datetime import datetime, timedelta
# print(datetime.now())
# print(datetime.now() + timedelta(seconds=3))

from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def times(x, y):
    res = x * y
    print(f'Hasil kali dari {x} dan {y} adalah {res}')
    return res

@app.task
def substract(x, y):
    res = x - y
    print(f'Hasil pengurangan dari {x} dan {y} adalah {res}')
    return x - y