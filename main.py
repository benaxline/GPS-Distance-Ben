from findClosestPoint import findClosestPoints
from distanceBetween import distanceBetween

def main():
    print('Enter array1, then array2...\n')
    
    n1 = int(input(f"How many coordinates in array1? "))
    coords1 = []
    for i in range(n1):
        raw = input(f"  Enter lat and lon for array1[{i}] (e.g. '34.803 40.323'): ")
        lat_str, lon_str = raw.split()
        coords1.append((float(lat_str), float(lon_str)))

    n2 = int(input(f"How many coordinates in array2? "))
    coords2 = []
    for i in range(n2):
        raw = input(f"  Enter lat and lon for array2[{i}] (e.g. '34.803 40.323'): ")
        lat_str, lon_str = raw.split()
        coords2.append((float(lat_str), float(lon_str)))
    
    print("\nClosest Points...\n")

    results = findClosestPoints(array1=coords1, array2=coords2)

    for i, point in enumerate(coords1):
        print(f"  array1[{i}] = {point}  |  closest in array2 is {results[i]}.")

if __name__ == "__main__":
    main()