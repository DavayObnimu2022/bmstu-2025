from abc import ABC, abstractmethod

class Vacancy(ABC):
    """Абстрактный класс вакансии"""
    @abstractmethod
    def get_description(self):
        pass

class ProgrammerVacancy(Vacancy):
    """Конкретная вакансия программиста"""
    def get_description(self):
        return "Программист Python"

class AnalystVacancy(Vacancy):
    """Конкретная вакансия аналитика"""
    def get_description(self):
        return "Аналитик данных"

class VacancyFactory:
    """Фабрика создания вакансий"""
    @staticmethod
    def create_vacancy(vacancy_type):
        if vacancy_type == "programmer":
            return ProgrammerVacancy()
        elif vacancy_type == "analyst":
            return AnalystVacancy()
        raise ValueError("Неизвестный тип вакансии")
