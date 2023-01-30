import unittest

from AkvoDataSeeder import data_seeder


class TestExample(unittest.TestCase):
    def test_add(self):
        self.assertEqual((data_seeder(5) + data_seeder(6)).value, 11)


if __name__ == '__main__':
    unittest.main()
