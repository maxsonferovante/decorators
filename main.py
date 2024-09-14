import time 
from decorator import cron

@cron.Cron(cron.CronExpression.EVERY_5_SECONDS)
def print_long_duration(*args, **kwargs):
    print("aqui")

@cron.Interval(cron.IntervalParams(
    name = "IntervalParams Custom 5 seconds",
    seconds=5))
def print_interval(*args, **kwargs):
    print("every 5 seconds")

cron.scheduler.start()
print_long_duration()
print_interval()

while True:
    time.sleep(0.01)

