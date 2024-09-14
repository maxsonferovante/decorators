from pydantic.dataclasses import dataclass

@dataclass
class IntervalParams:
    name: str = "IntervalParams"
    interval: int = 1
    seconds: int = 0
    minutes: int = 0
    hours: int = 0
    days: int = 0
    weeks: int = 0