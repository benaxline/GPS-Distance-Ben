from findClosestPoint import findClosestPoints
from inputDecisions import chooseArrayData
import logging


def main():
    print('Configuring arrays...')
    array1 = chooseArrayData("arr1")
    array2 = chooseArrayData("arr2")
    logging.info(f'array1: {array1}')
    logging.info(f'array2 {array2}')

    results = findClosestPoints(array1, array2)
    print('\nClosest Point:\n')

    for i, res in enumerate(results):
        array1Info = res['array1Data']
        array2Info = res['closestArray2Data']
        distance = res['distance']

        print(f'arr1[{i}] --> distance={distance} km\n')
        print(f'array 1 data: {array1Info}')
        print(f'closest array 2 data: {array2Info}\n')


if __name__ == "__main__":
    main()
