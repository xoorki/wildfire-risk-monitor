import csv
import time


def risk(temp, humidity, soil_moisture, windspeed):
    fire_risk = 0 
    fire_risk += ((temp - 20) / 15) * 25

    if humidity < 40:
        fire_risk += ((40 - humidity) / 40) * 30

    if soil_moisture < 25:
        fire_risk += ((25 - soil_moisture) / 25) * 20

    if windspeed > 5:
        fire_risk += ((windspeed - 5) / 10) * 25

    fire_risk = min(fire_risk, 100)
    return fire_risk

with open('BR2_rawData.csv', newline='') as f:
    csvreader = csv.DictReader(f)

    averages = []
    
    for row in csvreader:
        averages.append(row)

        if len(averages) == 30:

            avg_temp = sum(int(r['MB_Temp']) for r in averages) / 30
            avg_humidity = sum(int(r['MB_Humidity']) for r in averages) / 30
            avg_soil = sum(int(r['MB_soilMoisture']) for r in averages) / 30
            avg_wind = sum(int(r['ext_windSpeed']) for r in averages) / 30
            fire_risk = risk(avg_temp, avg_humidity, avg_soil, avg_wind)
            
            if fire_risk >= 76:
                alert = "VERY HIGH RISK! Trigger alarm!"
                
            elif fire_risk >= 56:
                alert = "MEDIUM RISK"
                
            else:
                alert = "SAFE"
                
            time.sleep(2)
            print("\n")
            print("Averages:")
            print("Temp:", avg_temp)
            print("Humidity:", avg_humidity)
            print("Soil Moisture:", avg_soil)
            print("Wind Speed:", avg_wind)
            print("Wildfire Risk:", fire_risk, "this is", alert)
            print("\n")


            averages = []
            

      

print("You have ran out of data to test on your csv file")

