# wildfire Risk Monitor

A micro:bit embedded system that monitors environmental conditions linked to wildfires and calculates wildfire risk in real time, built for my **2026 Leaving Certificate Computer Science** coursework project.

## About

Wildfires are becoming a bigger problem in Europe, with serious fires in Spain, Portugal and even Ireland in recent years. This project monitors the four main coire risk: **temperature, humidity, soilmoisture and wind speed**. It uses them to decide whether conditions are safe or dangerous.

The project has two parts:
- **Embedded system:** a micro:bit with sensotes risk live, and sets off an alarm when riskis high
- **Python model:** reads the logged data, cand runs "what if" scenarios

## Features

- Reads temperature, humidity, soil moisture d
- **Button A** starts logging, **Button B** shows current readings on the OLED screen, **A+B** stops logging
- Shows the risk level on the micro:bit:
  - 😀 happy face: safe
  - ❗ exclamation mark: medium risk
  - 💀 skull + buzzer alarm: very high risk
- Saves all readings to a CSV file for analys
- Calculates risk from **30-second averages** instead of single readings, for more accurate results
- Two what-if simulations to test how risk chwindier conditions

## Hardware

- BBC micro:bit
- Agriculture micro:bit kit
- Temperature sensor
- Humidity sensor
- Soil moisture sensor
- Wind speed anemometer
- OLED display
- Buzzer

## Built with

- **Python:** `pyserial`, `csv`, `pandas`
- **Thonny**
- **Microsoft MakeCode**

## Files

| File | What it does |
|------|--------------|
| `br2.py` | Reads sensor data from the micro:bit over USB serial and saves it to `BR2_rawData.csv` |
| `new_ar1.py` | Main risk model: reads the Cges each sensor and calculates the risk |
| `what_if.py` | Runs what-if scenarios on the collected data |
| `website.html` | My full coursework report

## How the risk is calculated

Each sensor adds to a risk score out of 100:

| Condition | Adds up to |
|-----------|-----------|
| Temperature above 20°C | 25 points (scaled
| Humidity below 40% | 30 points |
| Soil moisture below 25 | 20 points |
| Wind speed above 5 | 25 points |

| Score | Risk level |
|-------|------------|
| 76+ | 🔴 VERY HIGH RISK |
| 56–75 | 🟠 MEDIUM RISK |
| below 56 | 🟢 SAFE |

## What-if scenarios

- **Option A (drought):** temperature +20%, soil moisture −25%
- **Option B (hot and windy):** temperature +

## How to run it

1. Flash the micro:bit code using [Microsoft .microbit.org).
2. Plug the micro:bit into your computer with USB.
3. Install the libraries:
   ```
   pip install pyserial pandas
   ```
4. In `br2.py`, change `"COM17"` to your micrto log data:
   ```
   python br2.py
   ```
5. Press **Button A** on the micro:bit to stap.
6. Run the risk model:
   ```
   python new_ar1.py
   ```
7. Or try a what-if scenario:
   ```
   python what_if.py
   ```

## Testing

I tested each sensor by changing its conditior for temperature, breathing on the humiditysensor, using a damp paper towel for soil moisture, and bringing in a fan to spin the anemometer. I checked that the
system switched correctly between all three r

## What I learned

- Connecting analogue and digital sensors to wiring and pin problems
- Sending data from a micro:bit to a computer over serial and saving it as CSV
- Averaging data in batches for more reliablengs
- Cleaning and analysing data with pandas
- Building and testing a simulation model

## Future improvements

- Save each logging session to its own timest't overwritten
- Store data in a cloud database for long-term monitoring
