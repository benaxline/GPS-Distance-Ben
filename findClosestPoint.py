from distanceBetween import distanceBetween


def findClosestPoints(array1, array2):
    results = []
    for r in array1:
        lat1 = r["latitude"]
        lon1 = r["longitude"]

        minDist = float('inf')
        best = None

        for row in array2:
            lat2, lon2 = row['latitude'], row['longitude']
            dist = distanceBetween(lat1, lon1, lat2, lon2)
            if dist < minDist:
                minDist = dist
                best = row

        results.append({
            "array1Data": r['rowData'],
            "closestArray2Data": best['rowData'],
            "distance": round(minDist, 3)
        })
    return results
