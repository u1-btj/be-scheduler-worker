from apscheduler.schedulers.background import BlockingScheduler
from tasks import add

# Creates a default Background Scheduler
sched = BlockingScheduler()

def job_test(): # worker task
    add.delay(4, 5)

sched.add_job(job_test,'interval', seconds=5) # scheduler jalan setiap 5 detik (interval)
sched.start()