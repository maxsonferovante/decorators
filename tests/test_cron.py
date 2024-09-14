import pytest
from unittest.mock import patch, MagicMock
from app.scheduler import Cron, Interval, scheduler
from app.enums.cronExpressionEnum import CronExpression
from app.models.intervalParams import IntervalParams


@patch('decorator.cron')  # Mock da função add_job do scheduler
def test_cron_job(mock_add_job):
    # Função de exemplo
    @Cron(CronExpression.EVERY_5_MINUTES)
    def example_task():
        return "Task executed"

    # Chamando a função decorada
    example_task()

    # Verificando se o método add_job foi chamado com os argumentos corretos
    mock_add_job.assert_called_once_with(
        example_task, 
        trigger=CronExpression.EVERY_5_MINUTES.value, 
        id='example_task'
    )


@patch('decorator.cron')  # Mock da função add_job do scheduler
def test_interval_job(mock_add_job):
    # Função de exemplo
    @Interval(IntervalParams(seconds=10))
    def example_task():
        return "Task executed"

    # Chamando a função decorada
    example_task()

    # Verificando se o método add_job foi chamado com os parâmetros corretos
    mock_add_job.assert_called_once_with(
        example_task, 
        trigger='interval',  # O valor que você utiliza no SchedulerTypes.INTERVAL
        seconds=10,
        minutes=0,
        hours=0,
        days=0,
        weeks=0,
        id='example_task'
    )
