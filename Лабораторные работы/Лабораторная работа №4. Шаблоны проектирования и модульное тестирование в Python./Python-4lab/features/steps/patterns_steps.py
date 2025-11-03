from behave import *
from lab_python_fp import (
    VacancyFactory,
    ProgrammerVacancy,
    SalaryAdapter,
    LegacySalarySystem,
    VacancyProcessor,
    PositionFilterStrategy
)

@given('Фабрика вакансий')
def step_impl(context):
    context.factory = VacancyFactory

@when('Создаем вакансию программиста')
def step_impl(context):
    context.vacancy = context.factory.create_vacancy("programmer")

@then('Получаем вакансию с описанием "Программист Python"')
def step_impl(context):
    assert isinstance(context.vacancy, ProgrammerVacancy)
    assert context.vacancy.get_description() == "Программист Python"

@given('Адаптер системы зарплат')
def step_impl(context):
    context.adapter = SalaryAdapter(LegacySalarySystem())

@when('Рассчитываем зарплату для "Программист Python"')
def step_impl(context):
    context.salary = context.adapter.calculate_salary("Программист Python")

@then('Получаем зарплату 120000')
def step_impl(context):
    assert context.salary == 120000

@given('Процессор вакансий с фильтром программистов')
def step_impl(context):
    context.processor = VacancyProcessor(PositionFilterStrategy("Программист"))

@when('Фильтруем список вакансий')
def step_impl(context):
    context.vacancies = [
        {"position": "Программист Python"},
        {"position": "Аналитик"},
        {"position": "Программист Java"}
    ]
    context.filtered = context.processor.process(context.vacancies)

@then('Получаем только вакансии программистов')
def step_impl(context):
    assert len(context.filtered) == 2
    assert all("Программист" in v["position"] for v in context.filtered)
