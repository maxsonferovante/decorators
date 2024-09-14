from pytz import utc
from functools import wraps

from apscheduler.schedulers.background import BackgroundScheduler

from enums.schedulerTypeEnum import SchedulerTypes
from enums.cronExpressionEnum import CronExpression
from models.intervalParams import IntervalParams

scheduler = BackgroundScheduler()
scheduler.configure(timezone=utc)

def Cron(cronExpression: CronExpression = CronExpression.EVERY_MINUTE):
    def decorator_cron(func):
        def wrapper_cron(*args, **kwargs):
            try:             
                if not isinstance(cronExpression, CronExpression):
                    raise Exception("Invalid cron expression")   
                scheduler.add_job(func, trigger=cronExpression.value, id = func.__name__)                
            except Exception as e:
                raise e
        return wrapper_cron
    return decorator_cron

def Interval(IntervalParams: IntervalParams):
    def decorator_interval(func):
        def wrapper_interval(*args, **kwargs):
            try:
                scheduler.add_job(func, trigger = SchedulerTypes.INTERVAL.value[0], 
                                  seconds = IntervalParams.seconds,
                                  minutes = IntervalParams.minutes,
                                  hours = IntervalParams.hours,
                                  days = IntervalParams.days,
                                  weeks = IntervalParams.weeks,
                                  id = func.__name__)                
            except Exception as e:
                raise e
        return wrapper_interval
    return decorator_interval