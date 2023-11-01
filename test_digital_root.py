import pytest

from main import digital_root


def test_digital_root_two_digits():
  assert digital_root(16) == 7

def test_digital_root_three_digits():
  assert digital_root(942) == 6

def test_digital_root_large_number():
  assert digital_root(132189) == 6

def test_digital_root_single_digit():
  assert digital_root(5) == 5

def test_digital_root_negative_number():
  assert digital_root(-10) == -1
