from distanceBetween import readLatLonFromCSV
from handleLatLon import parse_value
import csv


def readCSVFile(filePath):
    possibleLatKeys = ['latitude', 'lat', 'Latitude']
    possibleLonKeys = ['longitude', 'lng', 'Longitude']
    output = []
    with open(filePath, 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        if reader.fieldnames:
            fieldNames = [fn.lower() for fn in reader.fieldnames]
        else:
            fieldNames = []

        latCol, lonCol = None, None

        for latCandidate in possibleLatKeys:
            if latCandidate in fieldNames:
                latCol = latCandidate
                break
        for lonCandidate in possibleLonKeys:
            if lonCandidate in fieldNames:
                lonCol = lonCandidate
                break

        if not latCol or not lonCol:
            raise ValueError(
                f'Could not find latitude/longitude columns in {filePath}'
                f'Looking for these latitude names: {possibleLatKeys} \n '
                f'and these longitude names: {possibleLonKeys} \n'
            )

        for row in reader:
            latitude = row.get(latCol, "")
            longitude = row.get(lonCol, "")

            latitude = parse_value(latitude)
            longitude = parse_value(longitude)

            if not latitude or not longitude:
                print(f'Skipping row (latitude or longitude empty) {row}...')
                continue

            try:
                lat = float(latitude)
                lon = float(longitude)
            except ValueError:
                print(f'Skipping row (invalid conversion): {row}...')
                continue

            output.append({
                "latitude": lat,
                "longitude": lon,
                "rowData": row
            })
    return output


def readSingleValue():
    line = input('Enter a single coordinate (30.082 -74.232): ').strip()
    latVal, lonVal = line.split()
    lat = float(latVal)
    lon = float(lonVal)
    return [{
        "latitude": lat,
        "longitude": lon,
        "rowData": f"(userInput) latitude={lat}, longitude={lon}"
    }]


def readInputChoice(choice):
    if choice == '1':
        # manual entry
        print('Enter number of coordinates: ')

    else:
        # CSV file
        csvPath = input('Enter the CSV path: ')
        readLatLonFromCSV(csvPath)


def chooseArrayData(arrayName):
    print('\nLoad {arrayName} from a CSV file or enter a single coordinate...')
    choice = input("Type 'csv' or 'single': ").strip().lower()

    if choice == "csv":
        path = input(f'Enter path to {arrayName} CSV: ')
        return readCSVFile(path)
    elif choice == 'single':
        return readSingleValue()
    else:
        print("Invalid Choice... Please type 'csv' or 'single'.")
        return chooseArrayData(arrayName=arrayName)
