import math
import csv


def distanceBetween(latitude1, longitude1, latitude2, longitude2):
    # Using haversine formula
    R = 6371.0

    # convert deg to rads
    phi1 = math.radians(latitude1)
    phi2 = math.radians(latitude2)
    lambda1 = math.radians(longitude1)
    lambda2 = math.radians(longitude2)

    dPhi = phi2 - phi1
    dLambda = lambda2 - lambda1

    a = (math.sin(dPhi / 2) ** 2
         + math.cos(phi1) * math.cos(phi2) * math.sin(dLambda / 2) ** 2)
    if a < 0:
        a = 0.0
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R*c


def readLatLonFromCSV(csvFilePath):
    with open(csvFilePath, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    return rows


def findClosestRow(row, data):
    lat1 = float(row["latitude"])
    lon1 = float(row["longitude"])

    minDist = float('inf')
    bestRow = None

    for r in data:
        lat2 = float(r["latitude"])
        lon2 = float(r["longitude"])
        dist = distanceBetween(lat1, lon1, lat2, lon2)

        if dist < minDist:
            minDist = dist
            bestRow = r

    return bestRow, minDist
