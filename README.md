# Pico 2WD Obstacle Avoidance Robot

## Overview

This project is a beginner autonomous 2WD robot car built using a Raspberry Pi Pico, TB6612FNG motor driver, two TT DC motors, and an HC-SR04 ultrasonic sensor.

The robot moves forward. When the ultrasonic sensor detects an obstacle in front of the robot, it stops, reverses briefly, turns, and continues moving.

## Features

- Raspberry Pi Pico control
- MicroPython program
- TB6612FNG dual motor driver
- PWM motor speed control
- Forward, backward, left turn, right turn, and stop functions
- HC-SR04 ultrasonic obstacle detection
- Voltage divider protection for Raspberry Pi Pico GPIO
- LED obstacle status indicator
- Motor direction correction variables
- Motor speed trim variables for calibration
- Basic autonomous obstacle-avoidance behavior

## Hardware Used

- Raspberry Pi Pico
- TB6612FNG motor driver
- 2WD robot chassis
- 2 TT DC motors
- HC-SR04 ultrasonic sensor
- 4xAA battery holder
- AA NiMH batteries 
- Breadboard
- Jumper wires
- Resistors for Echo voltage divider
- LED
- 220 ohm resistor for LED

## Wiring Summary

### Power

Battery positive is connected to:

- Raspberry Pi Pico VSYS
- TB6612FNG VM

Battery negative is connected to:

- Raspberry Pi Pico GND
- TB6612FNG GND
- HC-SR04 GND

Raspberry Pi Pico 3V3 OUT is connected to:

- TB6612FNG VCC

The Pico GND, TB6612FNG GND, battery negative, and HC-SR04 GND must all share a common ground.

### Motor Driver Connections

| TB6612FNG Pin | Raspberry Pi Pico Pin |
|---|---|
| PWMA | GP0 |
| AIN1 | GP1 |
| AIN2 | GP2 |
| PWMB | GP3 |
| BIN1 | GP4 |
| BIN2 | GP5 |
| STBY | GP6 |

### Ultrasonic Sensor Connections

| HC-SR04 Pin | Connection |
|---|---|
| VCC | 5V |
| GND | Common GND |
| TRIG | Pico GP14 |
| ECHO | Voltage divider to Pico GP15 |

The HC-SR04 Echo pin outputs 5V when the sensor is powered from 5V. Since Raspberry Pi Pico GPIO pins are 3.3V only, the Echo signal is connected through a voltage divider.

### Echo Voltage Divider

```text
HC-SR04 ECHO
     |
    1kΩ
     |
     +------ Pico GP15
     |
    2kΩ
     |
    GND
```

### LED Status Indicator

| Component | Connection |
|---|---|
| LED anode | Pico GP20 through 330 ohm resistor |
| LED cathode | GND |

The LED turns on when an obstacle is detected.

## Obstacle Avoidance Logic

1. Move forward normally.
2. Measure distance using the HC-SR04 ultrasonic sensor.
3. If the measured distance is below the obstacle threshold:
   - Turn on LED
   - Stop
   - Reverse briefly
   - Stop again
   - Turn
   - Continue moving
4. If no obstacle is detected:
   - Turn off LED
   - Continue moving forward


## Future Improvements

- Add better ultrasonic distance filtering.
- Add random left/right turn selection.
- Mount the ultrasonic sensor on a servo for left, front, and right scanning.
- Add wheel encoders for odometry.
- Add basic grid-based mapping.
- Add line-following mode using IR sensors.
- Add Raspberry Pi 5 visualization in a later version.

## Demo

## Project Status

Basic movement and ultrasonic obstacle avoidance are working.
