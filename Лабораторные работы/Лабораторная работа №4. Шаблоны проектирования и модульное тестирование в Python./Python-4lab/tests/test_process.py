import unittest
from unittest.mock import patch
from lab_python_fp.process_data import DataProcessor

class TestDataProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = DataProcessor()
        self.test_data = [
            {'job-name': 'Программист Python'},
            {'job-name': 'Аналитик'},
            {'job-name': 'Программист Java'}
        ]

    def test_f1_sorts_and_returns_unique_names(self):
        result = self.processor.f1(self.test_data)
        self.assertEqual(result, ['Аналитик', 'Программист Java', 'Программист Python'])

    def test_f2_filters_only_programmers(self):
        names = ['Программист Python', 'Аналитик', 'Программист Java']
        result = self.processor.f2(names)
        self.assertEqual(result, ['Программист Python', 'Программист Java'])

    @patch('lab_python_fp.process_data.gen_random')
    def test_f4_with_mocked_salaries(self, mock_gen):
        mock_gen.return_value = [150000, 180000]
        result = self.processor.f4(['Job1', 'Job2'])
        self.assertEqual(result, [
            'Job1, зарплата 150000 руб.',
            'Job2, зарплата 180000 руб.'
        ])
        mock_gen.assert_called_once_with(2, 100000, 200000)

if __name__ == '__main__':
    unittest.main()
