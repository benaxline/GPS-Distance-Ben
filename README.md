# GPS-Distance-Ben
Mission of the module:  If the user gives you two arrays of geo location, match each point in the first array to the closest one in the second array

## Important Files
`distanceBetween.py`: This file contains the function and logic to find the distance between two GPS points using the Haversine formula. This takes in four inputs, the first two represent the latitude and longitude of the first location and the next two represent the latitude and longitude of the second location. It will then return the distance between these two points.  

`findClosestPoint.py`: This file contains the function and logic to find the closest point in array2 for every GPS location in array 1. This takes in two arrays, `array1` and `array2`. It then cycles through each location in `array1`, finding the closest location in `array2`. It outputs a list of closest points that will correspond to the closest location to that in array 1. 


## How to Run
To run this program, you will want to use this command in the terminal:

`python main.py`

This will prompt you to first enter the number of coordinates in array 1, followed by entering the latitudes and longitudes of each location. You will then repeat this for array 2. An example of this is shown below.

<img width="697" alt="Screenshot 2025-01-22 at 4 30 23 PM" src="https://github.com/user-attachments/assets/264e42e2-5cea-4228-946e-13741e858593" />

