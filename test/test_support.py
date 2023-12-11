import unittest
from src.support import support as calc_support


class TestSupportCalculation(unittest.TestCase):

    def test_calculate_support(self):
        # Mock dataset
        dataset = [
            ['bread', 'milk'],
            ['bread', 'diaper', 'beer', 'eggs'],
            ['milk', 'diaper', 'beer', 'cola'],
            ['bread', 'milk', 'diaper', 'beer'],
            ['bread', 'milk', 'diaper', 'cola']
        ]
        itemset = ['bread', 'milk']

        # Expected support
        expected_support = 3 / 5  # Adjust this based on your support calculation logic

        # Calculate support
        support = calc_support(dataset, itemset)

        # Assert
        self.assertEqual(support, expected_support)


if __name__ == '__main__':
    unittest.main()
