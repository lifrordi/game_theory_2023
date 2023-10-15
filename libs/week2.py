from typing import List, Optional
from scipy.optimize import linprog
import numpy as np

def verify_support_one_side(matrix: np.array, support_row: List, support_col: List) -> Optional[List]:
    """Tries to see whether the column player can mix their strategies in the support so that the values of the row player are best-responding"""
    return None
