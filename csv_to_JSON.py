import csv
import json


def make_json(csvFilePath, jsonFilePath):
    data = {}
    with open(csvFilePath, encoding="utf-8") as csvf:
        csvReader = csv.DictReader(csvf)

        for rows in csvReader:
            key = rows["_id"]
            data[key] = rows

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dump(data, indent=4))


make_json('Boston 311 012225.csv', 'firstJson.json')
