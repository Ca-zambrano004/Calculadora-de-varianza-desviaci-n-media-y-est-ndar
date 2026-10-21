import unittest
import mean_var_std

class TestCalculate(unittest.TestCase):
    def test_calculate_correct(self):
        # Caso de prueba con lista de 9 números
        result = mean_var_std.calculate([0,1,2,3,4,5,6,7,8])
        expected_mean = [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0]
        self.assertEqual(result['mean'], expected_mean)
        self.assertEqual(result['max'], [[6, 7, 8], [2, 5, 8], 8])
        self.assertEqual(result['min'], [[0, 1, 2], [0, 3, 6], 0])
        self.assertEqual(result['sum'], [[9, 12, 15], [3, 12, 21], 36])

    def test_calculate_invalid_length(self):
        # Caso de prueba con lista de menos de 9 números
        with self.assertRaises(ValueError) as context:
            mean_var_std.calculate([1,2,3])
        self.assertEqual(str(context.exception), "List must contain nine numbers.")

if __name__ == "__main__":
    unittest.main()
