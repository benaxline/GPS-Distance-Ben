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

def test_1_degree_longitude_atEquator():
    lat1, lon1 = 0, 0
    lat2, lon2 = 0, 1

    distance = distanceBetween(latitude1=lat1, longitude1=lon1, latitude2=lat2, longitude2=lon2)
    assert distance == pytest.approx(111.32, abs=1.0)

def test_oppositePointsOnEarth():
    lat1, lon1 = 0, 0
    lat2, lon2 = 0, 180
    distance = distanceBetween(latitude1=lat1, longitude1=lon1, latitude2=lat2, longitude2=lon2)
    expected_distance = 20037.5
    assert distance == pytest.approx(expected=expected_distance, abs=100)

def test_knownCities():
    # testing NYC and LA
    NYC_lat, NYC_lon = 40.7128, 74.0060
    LA_lat, LA_lon = 34.0549, 118.2426
    distance = distanceBetween(NYC_lat, NYC_lon, LA_lat, LA_lon)
    expected_distance = 3935.74
    assert distance == pytest.approx(expected_distance, abs=100)