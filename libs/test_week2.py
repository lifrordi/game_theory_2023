import libs.week2 as week2
import numpy as np
import pytest
import numpy.testing as nptest


def test_week1():
    matrix_p1 = np.array([[0, 0, -10], [1, -10, -10], [-10, -10, -10]])
    matrix_p2 = np.array([[0, 1, -10], [0, -10, -10], [-10, -10, -10]])


    result = week2.verify_support_one_side(matrix = matrix_p1, support_row=[0, 1], support_col = [0, 1, 2])
    nptest.assert_allclose(result, [0.90909, 0.09090], rtol=1e-3)


    result = week2.verify_support_one_side(matrix = matrix_p2.T, support_row=[0, 1, 2], support_col = [0, 1])
    assert result is None