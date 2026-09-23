

import serial
import csv

ser = serial.Serial("COM17", 115200, timeout = 5) #need to check if what COM# to use, timeout is 5 seconds so that if no data recieved program will stop and create the csv and also makes "serial.Serial("COM17", 115200, timeout = 5)" code into shortend "ser" for quick use in my code down the line

#click bottom right corner "local python 3" to see COM port for microbit

# line = ser.readline().decode("utf-8", errors="ignore").strip() #reads the line of info from the MB and checks for errors and 
# #strip is used to remove random spaces etc that were entered by accident

filename = "BR2_rawData.csv" #name i want of the csv file 

# Create a clean CSV and write header each time csv is run
with open(filename, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["MB_Temp", "MB_Humidity", "MB_soilMoisture", "ext_windSpeed"]) # these are the headers of the columns in the csv file

while True:
    
    
    line = ser.readline().decode("utf-8", errors="ignore").strip() 

    #if it cant read any more info it will say logging finish and break the loop
    if line == "":
        print("No data received for 5 seconds. Logging finished.")
        break
    
    #When button A+B is pressed on the micro:bit, it sends "END" via serial. This code checks if "END" was sent through the MB and if so notifies the user that logging has stopped and exits the loop.
    if line =="END": 
        print("Logging manually stopped on Microbit: button A+B pressed")
        break
    
    parts = line.split(",") # splits the information up using a comma ","
    
    
   #split up the information being fed in from inputs 
    MB_Temp = parts[0] 
    MB_Humidity = parts[1]
    MB_soilMoisture = parts[2] 
    ext_windSpeed = parts[3] 



    print("Temp:", MB_Temp, "\t  Humidity:", MB_Humidity, "\t Soil Moisture:", MB_soilMoisture, "\t Wind Speed:", ext_windSpeed) #  this is just to make sure that the information is coming in and the values are looking ok.

    with open(filename, "a", newline="") as f: # a is for append, w to rewrite
        writer = csv.writer(f)
        writer.writerow([MB_Temp, MB_Humidity, MB_soilMoisture ,ext_windSpeed]) # Write current sensor readings as a new row in the CSV file



print("BR2: csv file saved as", filename)

