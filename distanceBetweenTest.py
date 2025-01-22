import pytest
import math
from distanceBetween import distanceBetween

def test_same_coords():
    latitude, longitude = 0, 0

    distance = distanceBetween(latitude, longitude, latitude, longitude)

    assert distance == pytest.approx(0.0, abs=1e-6)

def test_1_deg_latitude():
    lat1, lon1 = 0, 0
    lat2, lon2 = 1, 0

    distance = distanceBetween(latitude1=lat1, longitude1=lon1, latitude2=lat2, longitude2=lon2)
    assert distance == pytest.approx(111.32, abs=1.0) # 1 degree is approx 111.32