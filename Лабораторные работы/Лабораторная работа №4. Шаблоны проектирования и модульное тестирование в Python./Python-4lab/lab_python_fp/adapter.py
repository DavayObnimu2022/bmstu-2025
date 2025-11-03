class LegacySalarySystem:
    """Старая система расчета зарплат"""
    def get_salary(self, position_code):
        salaries = {
            "DEV": 120000,
            "ANL": 90000,
            "MNG": 150000
        }
        return salaries.get(position_code, 0)

class SalaryAdapter:
    """Адаптер для современной системы зарплат"""
    def __init__(self, legacy_system):
        self.legacy_system = legacy_system

    def calculate_salary(self, position_name):
        """Новый интерфейс для работы с вакансиями"""
        code = self._get_position_code(position_name)
        return self.legacy_system.get_salary(code)

    def _get_position_code(self, position_name):
        codes = {
            "Программист": "DEV",
            "Аналитик": "ANL",
            "Менеджер": "MNG"
        }
        for key in codes:
            if key in position_name:
                return codes[key]
        return "UNK"
