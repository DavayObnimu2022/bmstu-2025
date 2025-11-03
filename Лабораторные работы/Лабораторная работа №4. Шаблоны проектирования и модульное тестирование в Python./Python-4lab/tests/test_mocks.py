from unittest import TestCase, mock
from lab_python_fp.process_data import DataProcessor


class TestWithMocks(TestCase):
    @mock.patch('lab_python_fp.process_data.gen_random')
    def test_f4_with_mocked_salaries(self, mock_gen):
        mock_gen.return_value = [150000, 180000]
        processor = DataProcessor()
        result = processor.f4(['Job1', 'Job2'])

        self.assertEqual(result, [
            'Job1, зарплата 150000 руб.',
            'Job2, зарплата 180000 руб.'
        ])
        mock_gen.assert_called_once_with(2, 100000, 200000)
