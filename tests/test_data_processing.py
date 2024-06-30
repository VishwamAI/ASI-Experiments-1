import unittest
import pandas as pd
import numpy as np
from learning.data_processing import handle_missing_values

class TestDataProcessing(unittest.TestCase):

    def setUp(self):
        # Sample DataFrame for testing
        self.df = pd.DataFrame({
            'A': [1, 2, np.nan, 4],
            'B': [np.nan, 2, 3, 4],
            'C': [1, np.nan, np.nan, 4]
        })

    def test_handle_missing_values_mean(self):
        result = handle_missing_values(self.df, strategy='mean')
        expected = pd.DataFrame({
            'A': [1, 2, 2.333333, 4],
            'B': [3.0, 2, 3, 4],
            'C': [1, 2.5, 2.5, 4]
        })
        pd.testing.assert_frame_equal(result, expected, check_dtype=False)

    def test_handle_missing_values_median(self):
        result = handle_missing_values(self.df, strategy='median')
        expected = pd.DataFrame({
            'A': [1, 2, 2, 4],
            'B': [3.0, 2, 3, 4],
            'C': [1, 2.5, 2.5, 4]
        })
        pd.testing.assert_frame_equal(result, expected, check_dtype=False)

    def test_handle_missing_values_mode(self):
        result = handle_missing_values(self.df, strategy='mode')
        expected = pd.DataFrame({
            'A': [1, 2, 1, 4],
            'B': [2.0, 2, 3, 4],
            'C': [1, 1, 1, 4]
        })
        pd.testing.assert_frame_equal(result, expected, check_dtype=False)

    def test_handle_missing_values_constant(self):
        result = handle_missing_values(self.df, strategy='constant', fill_value=0)
        expected = pd.DataFrame({
            'A': [1, 2, 0, 4],
            'B': [0, 2, 3, 4],
            'C': [1, 0, 0, 4]
        })
        pd.testing.assert_frame_equal(result, expected, check_dtype=False)

    def test_handle_missing_values_drop(self):
        result = handle_missing_values(self.df, strategy='drop')
        expected = pd.DataFrame({
            'A': [4.0],
            'B': [4.0],
            'C': [4.0]
        }, index=[3])
        pd.testing.assert_frame_equal(result, expected, check_dtype=False)

    def test_handle_missing_values_invalid_strategy(self):
        with self.assertRaises(ValueError):
            handle_missing_values(self.df, strategy='invalid')

    def test_handle_missing_values_constant_no_fill_value(self):
        with self.assertRaises(ValueError):
            handle_missing_values(self.df, strategy='constant')

if __name__ == '__main__':
    unittest.main()