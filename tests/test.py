"""
Primary script to test the order_book_weight
"""

import pytest

from src.algo.order_book.order_book_weight import weighted_sum


# unit tests for order_book_weight.py

@pytest.fixture
def data_weighted_sum():
    return [[1, 0.1], [2, 0.2], [3, 0.3], [4, 0.4], [5, 0.5], [6, 0.6]]


@pytest.fixture
def result_weighted_sum():
    return 4.333333333333333


def test_weighted_sum(data_weighted_sum, result_weighted_sum):
    assert round(weighted_sum(data_weighted_sum), 6) == \
           round(result_weighted_sum, 6)

