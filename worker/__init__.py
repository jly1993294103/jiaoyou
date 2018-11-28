import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jiaoyou.settings')

celery_app = Celery('jiaoyou')
celery_app.config_from_object('worker.config')
celery_app.autodiscover_tasks()

def call_by_worker(func):
    task = celery_app.task(func)
    return task.delay