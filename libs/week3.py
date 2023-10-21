import numpy as np
import libs.week1 as week1


def compute_deltas(matrix: np.array, row_strategy: np.array, column_strategy: np.array) -> np.array:
    """Computer how much the players could improve if they were to switch to a best response"""    
    return np.array([0.0, 0.0])


def compute_exploitability(matrix: np.array, row_strategy: np.array, column_strategy: np.array) -> float:
    return 0.0


def compute_epsilon(matrix: np.array, row_strategy: np.array, column_strategy: np.array) -> float:
    """Computes epsilon as defined for epsilon-Nash equilibrium"""
    return 0.0


def compute_exploitability_zero_sum(matrix: np.array, row_strategy: np.array, column_strategy: np.array) -> float:
    """Compute exploitability for a zero-sum game"""
    return 0.0