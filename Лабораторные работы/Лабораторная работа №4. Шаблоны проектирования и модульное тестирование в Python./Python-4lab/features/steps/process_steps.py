from behave import *
from lab_python_fp.process_data import DataProcessor

@given('имеются данные о вакансиях')
def step_impl(context):
    context.processor = DataProcessor()
    context.data = [
        {'job-name': 'Программист Python'},
        {'job-name': 'Аналитик'},
        {'job-name': 'Программист Java'}
    ]

@when('применяется конвейер обработки')
def step_impl(context):
    context.result = context.processor.process_pipeline(context.data)

@then('получаем только вакансии программистов с Python и зарплатой')
def step_impl(context):
    assert len(context.result) == 2
    assert all('Программист' in job for job in context.result)
    assert all('с опытом Python' in job for job in context.result)
    assert all('зарплата' in job for job in context.result)
