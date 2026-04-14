import unittest
from datetime import datetime, timedelta
import service

class TestStudentService(unittest.TestCase):
    def test_should_fail_when_student_is_underage(self):
        # 15 years ago
        underage_date = (datetime.now() - timedelta(days=15*365)).strftime('%Y-%m-%d')
        data = {
            "name": "John Doe", "birth_date": underage_date,
            "cpf": "123", "email": "j@doe.com", "phone": "123", "hometown": "Palmas"
        }
        res, status = service.create_student(data)
        self.assertEqual(status, 400)
        self.assertIn("must be of legal age", res['errors'][0])

    def test_should_fail_when_not_from_capital(self):
        data = {
            "name": "Jane Doe", "birth_date": "1990-01-01",
            "cpf": "456", "email": "jane@doe.com", "phone": "456", "hometown": "SmallTown"
        }
        res, status = service.create_student(data)
        self.assertEqual(status, 400)
        self.assertIn("Only students from capitals", res['errors'][0])