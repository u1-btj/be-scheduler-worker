from apscheduler.schedulers.background import BlockingScheduler
from tasks import times, substract
from random import randint
from datetime import datetime, timedelta
import csv

scheduler = BlockingScheduler()
header = ['Waktu', 'Angka1', 'Angka2', 'Hasil']
end_trigger = 0

def logging(record):
    with open('record_result.csv', 'a+', newline='') as file_csv:
        write_file = csv.writer(file_csv)
        write_file.writerow(record)

def get_rand_num():
    return randint(0, 100)

def job_times():
    num1 = get_rand_num()
    num2 = get_rand_num()
    result = times(num1, num2)
    times.delay(num1, num2)
    logging([str(datetime.now()), num1, num2, result])

def job_substract():
    num1 = get_rand_num()
    num2 = get_rand_num()
    result = substract(num1, num2)
    substract.delay(num1, num2)
    logging([str(datetime.now()), num1, num2, result])

def job_shutdown():
    global end_trigger
    if end_trigger == 0:
        end_trigger = 1
    else:
        scheduler.remove_all_jobs()
        scheduler.shutdown(wait=False)

logging(header)
scheduler.add_job(job_times, 'interval', seconds=9, id='times_job', start_date=str(datetime.now()), end_date=str(datetime.now() + timedelta(minutes=3)))
scheduler.add_job(job_substract, 'cron', second='*/10', id='substract_job', start_date=str(datetime.now()), end_date=str(datetime.now() + timedelta(minutes=3)))
scheduler.add_job(job_shutdown, 'interval', minutes=3, seconds=5) # Job shutdown to stop the scheduler after 3 minute and 5 second. Allocate 5 second to make sure all jobs completed on appropriate end date.
print(f"Executing until {str(datetime.now() + timedelta(minutes=3))}")
scheduler.start()
print("Finish.")
exit()
