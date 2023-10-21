import libs.week3 as week3
import numpy as np
import pytest


def test_week3():
    matrix = np.array([[0, 1, -1], [-1, 0, 1], [1, -1, 0]])
    row_strategy = np.array([[0.1, 0.2, 0.7]])
    column_strategy = np.array([[0.3, 0.2, 0.5]]).transpose()

    delta_row, delta_column = week3.compute_deltas(matrix=matrix, row_strategy=row_strategy,
                                                   column_strategy=column_strategy)
    assert delta_row == pytest.approx(0.12)
    assert delta_column == pytest.approx(0.68)