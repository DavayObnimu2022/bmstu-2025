import unittest
from classes import StoredProcedure, Database, StoredProcedureDatabase
from queries import find_procedures_ending_with_ov, average_salary_by_database, databases_starting_with_a

class TestQueries(unittest.TestCase):
    def setUp(self):
        self.databases = [
            Database(1, "Административная"),
            Database(2, "Финансовая"),
            Database(3, "Отделов")
        ]
        self.procedures = [
            StoredProcedure(1, "Процедураов", 1),  # 10 символов
            StoredProcedure(2, "Процедура", 2),  # 9 символов
            StoredProcedure(3, "Функцияов", 1),  # 11 символов
            StoredProcedure(4, "Функция", 3),  # 7 символов
        ]
        self.sp_dbs = [
            StoredProcedureDatabase(1, 1),
            StoredProcedureDatabase(2, 2),
            StoredProcedureDatabase(3, 1),
            StoredProcedureDatabase(4, 3),
        ]

    def test_find_procedures_ending_with_ov(self):
        result = find_procedures_ending_with_ov(self.procedures, self.databases)
        expected = [("Процедураов", "Административная"), ("Функцияов", "Административная")]
        self.assertEqual(result, expected)

    def test_average_salary_by_database(self):
        result = average_salary_by_database(self.procedures, self.databases)
        expected = [
            ("Отделов", 7.0),
            ("Финансовая", 9.0),
            ("Административная", 10.5)
        ]
        self.assertEqual(result, expected)

    def test_databases_starting_with_a(self):
        result = databases_starting_with_a(self.procedures, self.databases, self.sp_dbs)
        expected = [("Административная", ["Процедураов", "Функцияов"])]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()