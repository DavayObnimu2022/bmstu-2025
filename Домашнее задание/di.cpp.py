# Интерфейс (абстрактный класс)
from abc import ABC, abstractmethod
#рефакторинг  - улучшение переводится. С++ и Си Шарп для себя , питон не очень для развития
class Database(ABC):
    @abstractmethod
    def save(self, data: str) -> None:
        pass

# Реализация зависимости
class PostgreSQL(Database):
    def save(self, data: str) -> None:
        print(f"Сохранение '{data}' в PostgreSQL")

# Класс, принимающий зависимость через конструктор
class Service:
    def __init__(self, database: Database):
        self.database = database

    def process_data(self, data: str) -> None:
        self.database.save(data)

# Использование
db = PostgreSQL()
service = Service(db)
service.process_data("Привет, DI на Python!")