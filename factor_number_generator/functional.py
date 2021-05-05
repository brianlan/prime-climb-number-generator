import math
from collections import defaultdict
from functools import reduce
from typing import Dict

from tqdm import tqdm


def get_factors(number: int, use_tqdm: bool = False) -> Dict[int, int]:
    """Get all the factors and the corresponding frequency of a given number.

    Parameters
    ----------
    number : int
        the number needs to be factorized
    use_tqdm : bool
        if true, will show progress bar

    Returns
    -------
    Dict[int, int]
        the k-v are the factor and the frequency respectiely.

    Raises
    ------
    ValueError
        raises error if the number if less or equal 0
    """
    if number <= 0:
        raise ValueError(f"number should be a positive integer, but {number!r} is given.")
    upper = int(math.sqrt(number))
    factors = defaultdict(int)
    if use_tqdm:
        for i in tqdm(range(2, upper + 1), total=upper - 1):
            while number > 1 and number % i == 0:
                factors[i] += 1
                number //= i
    else:
        for i in range(2, upper + 1):
            while number > 1 and number % i == 0:
                factors[i] += 1
                number //= i
    if not factors:
        factors = {1: 1, number: 1}
    if number != 1:
        factors[number] = 1
    return factors
