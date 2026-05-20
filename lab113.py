#Creating a car inventory data
import csv
import copy

myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

for key, value in myVehicle.items():
    print("{} : {}".format(key,value)) #shortcut
    
myInventoryList = []

with open("car_fleet.csv") as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    linecount = 0
    columns = []
    for line in csvReader:
            if linecount == 0:
                columns = line
                print(f'Column names are:{",".join(line)}')
                linecount += 1 
                #shortcut -> linecount = linecount+1
            else:
                print(f'vin: {line[0]}, make: {line[1]}, model: {line[2]}, year: {line[3]}, range: {line[4]}, topSpeed: {line[5]}, zeroSixty: {line[6]}, mileage: {line[7]}')
              
                vehicle = {}
                for i in range(1, len(line)):
                    vehicle[columns[i]] = line[i]
                myInventoryList.append(vehicle)
        
    print(myInventoryList)
                