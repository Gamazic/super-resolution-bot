from celery import Celery


celery_app = Celery('tasks',
                    broker="redis://redis:6379",
                    backed="redis://redis:6379",
                    include=['project.celery_task_app.tasks'])
