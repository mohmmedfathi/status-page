
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from  jobs.py import do_anything

def start():
	scheduler = BackgroundScheduler()
	scheduler.add_job(do_anything, 'interval', seconds=2)
	scheduler.start()