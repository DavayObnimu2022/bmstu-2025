import unittest
from unittest.mock import Mock, patch
from lab_python_fp.factory_method import VacancyFactory, ProgrammerVacancy
from lab_python_fp.adapter import LegacySalarySystem, SalaryAdapter
from lab_python_fp.strategy import VacancyProcessor, PositionFilterStrategy

class TestFactoryMethod(unittest.TestCase):
    def test_create_programmer_vacancy(self):
        vacancy = VacancyFactory.create_vacancy("programmer")
        self.assertIsInstance(vacancy, ProgrammerVacancy)

class TestAdapterPattern(unittest.TestCase):
    def test_salary_calculation(self):
        legacy_system = LegacySalarySystem()
        adapter = SalaryAdapter(legacy_system)
        self.assertEqual(adapter.calculate_salary("Программист Python"), 120000)

class TestStrategyPattern(unittest.TestCase):
    def test_programmer_filter(self):
        processor = VacancyProcessor(PositionFilterStrategy("Программист"))
        vacancies = [
            {"position": "Программист Python"},
            {"position": "Аналитик"},
            {"position": "Программист Java"}
        ]
        filtered = processor.process(vacancies)
        self.assertEqual(len(filtered), 2)

if __name__ == '__main__':
    unittest.main()
