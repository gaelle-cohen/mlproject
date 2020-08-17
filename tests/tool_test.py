# -*- coding: UTF-8 -*-

# Import from standard library
import os
import mlproject
# Import from our lib
from mlproject.distance import haversine
import pytest


def test_clean_data():
    out = haversine(48.865070, 2.380009, 35, 93)
    assert round(out,2) == 10066.78

