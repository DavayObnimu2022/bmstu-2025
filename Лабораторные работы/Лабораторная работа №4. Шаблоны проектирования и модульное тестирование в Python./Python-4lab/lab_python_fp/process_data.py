import json
import sys
from .gen_random import gen_random
from .unique import Unique
from .print_result import print_result
from .cm_timer import cm_timer_1


class DataProcessor:
    """Класс для обработки данных о вакансиях"""

    @staticmethod
    def load_data(path):
        """Загрузка данных из JSON файла"""
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    @print_result
    def f1(self, data):
        """Этап 1: Уникальные названия с сортировкой"""
        job_names = [item['job-name'] for item in data]
        return sorted(Unique(job_names, ignore_case=True), key=str.lower)

    @print_result
    def f2(self, job_names):
        """Этап 2: Фильтрация программистов"""
        return [name for name in job_names if name.lower().startswith('программист')]

    @print_result
    def f3(self, job_names):
        """Этап 3: Добавление Python-опыта"""
        return [f"{name} с опытом Python" for name in job_names]

    @print_result
    def f4(self, job_names):
        """Этап 4: Добавление зарплат"""
        salaries = list(gen_random(len(job_names), 100000, 200000))
        return [f"{job}, зарплата {salary} руб." for job, salary in zip(job_names, salaries)]

    def process_pipeline(self, data):
        """Запуск полного конвейера обработки"""
        return self.f4(self.f3(self.f2(self.f1(data))))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python process_data.py <path_to_json>")
        sys.exit(1)

    processor = DataProcessor()
    data = processor.load_data(sys.argv[1])
    with cm_timer_1():
        result = processor.process_pipeline(data)
