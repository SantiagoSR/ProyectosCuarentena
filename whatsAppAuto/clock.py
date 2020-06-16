from apscheduler.schedulers.blocking import BlockingScheduler
from automessage import send_mms 


sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(send_mms, 'interval', seconds=20)

sched.start()

