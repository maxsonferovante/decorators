from enum import Enum

class SchedulerTypes(Enum):
    CRON = 'cron',
    DATE = 'date'
    INTERVAL = 'interval',
    