from abc import ABC, abstractmethod


class FilterStrategy(ABC):
    """Абстрактная стратегия фильтрации"""

    @abstractmethod
    def filter(self, vacancies):
        pass


class PositionFilterStrategy(FilterStrategy):
    """Конкретная стратегия фильтрации по должности"""

    def __init__(self, position_keyword):
        self.position_keyword = position_keyword

    def filter(self, vacancies):
        return [v for v in vacancies if self.position_keyword in v["position"]]


class VacancyProcessor:
    """Контекст, использующий стратегию"""

    def __init__(self, strategy):
        self.strategy = strategy

    def process(self, vacancies):
        return self.strategy.filter(vacancies)
