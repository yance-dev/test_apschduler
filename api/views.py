from django.shortcuts import render

# Create your views here.
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")

scheduler.start()

def time_task(task):
    print("I'm a test job!")

scheduler.add_job(time_task, "cron", id=task.name, hour=hour, minute=minute, second=0,kwargs={"task": task})
register_events(scheduler)