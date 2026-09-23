#What if Situations
#Temp is 20% degrees hotter and the soil is 25% drier

import pandas as pd

fire_risk = 0
#____________set the file path for cleaning_________

file_path = "BR2_rawData.csv" # tell python the name of the file andf file type (csv)

data = pd.read_csv(file_path, na_values = ["no data"]) #read the csv and replace empty data

#______________clean the data - remove special characters and blanks_______________


data = data.dropna() # removes any blank lines/data

numeric_cols = ["MB_Temp", "MB_soilMoisture", "MB_Humidity", "ext_windSpeed"]
for col in numeric_cols:
    data[col] = pd.to_numeric(data[col], errors = "coerce")

def risk(temp, humidity, soil_moisture, windspeed):
    fire_risk = 0
    fire_risk += ((temp - 20) / 15) * 25
    
    if humidity < 40:
        fire_risk += ((40 - humidity) / 40) * 30

    if soil_moisture < 25:
        fire_risk += ((25 - soil_moisture) / 25) * 20

    if windspeed > 5:
        fire_risk += ((windspeed - 5) / 10) * 25
    
    return min(fire_risk, 100)




print("Option A = Temp is 20% degrees hotter and the soil is 25% drier")
print("Option B = Wind speed is 40% faster and temp is 10% faster")
print("\n")
simulated_scenario = input("Which what if situation would you like to run? Option A or B ").upper()

results = []
averages = []

batch_number = 1

for index, row in data.iterrows():
    averages.append(row)

    if len(averages) == 30:

        if simulated_scenario == "A":
            avg_temp = sum(r['MB_Temp'] * 1.20 for r in averages) / 30
            avg_soil = sum(r['MB_soilMoisture'] * 0.75 for r in averages) / 30
            avg_humidity = sum(r['MB_Humidity'] for r in averages) / 30
            avg_wind = sum(r['ext_windSpeed'] for r in averages) / 30

        elif simulated_scenario == "B":
            avg_temp = sum(r['MB_Temp'] * 1.10 for r in averages) / 30
            avg_soil = sum(r['MB_soilMoisture'] for r in averages) / 30
            avg_humidity = sum(r['MB_Humidity'] for r in averages) / 30
            avg_wind = sum(r['ext_windSpeed'] * 1.40 for r in averages) / 30

        else:
            print("Invalid choice")
            break

        # Calculate risk
        fire_risk = risk(avg_temp, avg_humidity, avg_soil, avg_wind)
        results.append(fire_risk)

        print(f"Batch {batch_number}:")
        print("Wildfire Risk:", round(fire_risk, 2))

        if fire_risk >= 76:
            print("Condition: VERY HIGH RISK")
        elif fire_risk >= 56:
            print("Condition: MEDIUM RISK")
        else:
            print("Condition: SAFE")

        batch_number += 1
        averages = []  


if results:
    overall_avg = sum(results) / len(results)
    print("\nOverall Average Wildfire Risk:", round(overall_avg, 2))

    if overall_avg >= 76:
        print("Overall Condition: VERY HIGH RISK")
    elif overall_avg >= 56:
        print("Overall Condition: MEDIUM RISK")
    else:
        print("Overall Condition: SAFE")