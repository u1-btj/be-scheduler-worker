from apscheduler.schedulers.background import BlockingScheduler

# Creates a default Background Scheduler
sched = BlockingScheduler()

def prompt(): # task
    print("Executing Task...")

sched.add_job(prompt,'interval', seconds=5) # scheduler jalan setiap 5 detik (interval)
sched.start()
