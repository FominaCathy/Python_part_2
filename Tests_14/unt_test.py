import io
import unittest
from unittest.mock import patch

from prime import is_prime


class TestCaseName(unittest.TestCase):
    def test_method(self):
        self.assertEqual(2 * 2, 4, msg='Видимо и в этой вселенной не работает :-(')


class TestPrime(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(6))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_warning_true(self, moc_stdout):
        self.assertTrue(is_prime(100000007))
        self.assertEqual(moc_stdout.getvalue(),
                         "If the number P is prime, the check may take a long time. Working...\n")


if __name__ == '__main__':
    unittest.main(verbosity=2)
