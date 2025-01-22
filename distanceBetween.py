import math

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

    a = math.sin(dPhi/2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(dLambda/2)**2
    b = math.sqrt(a)
    d = 2 * R * math.asin(b)
    return d
