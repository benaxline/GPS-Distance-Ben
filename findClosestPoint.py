import distanceBetween

def findClosestPoints(array1, array2):
    closest_points = []
    for (lat1, lon1) in array1: 
        min_dist = float('inf')
        closest_point = None
        
        for (lat2, lon2) in array2:
            distance = distanceBetween(lat1, lon1, lat2, lon2)
            if distance < min_dist:
                min_dist = distance
                closest_point = (lat2, lon2)

        # add closest point to list
        closest_points.append(closest_point)

    return closest_points