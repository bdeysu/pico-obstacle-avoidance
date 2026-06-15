from machine import Pin, PWM, time_pulse_us
from time import sleep, sleep_us

# Motors configuration

# Right motor - Channel A
PWMA = PWM(Pin(0))
AIN1 = Pin(1, Pin.OUT)
AIN2 = Pin(2, Pin.OUT)

# Left motor - Channel B
PWMB = PWM(Pin(3))
BIN1 = Pin(4, Pin.OUT)
BIN2 = Pin(5, Pin.OUT)

STBY = Pin(6, Pin.OUT)

PWMA.freq(1000)
PWMB.freq(1000)
STBY.value(1)

# Ultrasonic sensor

TRIG = Pin(14, Pin.OUT)
ECHO = Pin(15, Pin.IN)

TRIG.value(0)

# Tuning

LEFT_TRIM = 1.00
RIGHT_TRIM = 1.00

LEFT_DIR = 1
RIGHT_DIR = 1

NORMAL_SPEED = 50
TURN_SPEED = 45
OBSTACLE_DISTANCE = 18  # cm

#LED
LED = Pin(20, Pin.OUT)

# Motor functions
def right_motor(speed):
    speed = speed * RIGHT_DIR

    if speed > 0:
        AIN1.value(1)
        AIN2.value(0)
    elif speed < 0:
        AIN1.value(0)
        AIN2.value(1)
    else:
        AIN1.value(0)
        AIN2.value(0)

    speed = abs(speed) * RIGHT_TRIM
    speed = max(0, min(100, speed))

    PWMA.duty_u16(int(speed * 65535 / 100))


def left_motor(speed):
    speed = speed * LEFT_DIR

    if speed > 0:
        BIN1.value(1)
        BIN2.value(0)
    elif speed < 0:
        BIN1.value(0)
        BIN2.value(1)
    else:
        BIN1.value(0)
        BIN2.value(0)

    speed = abs(speed) * LEFT_TRIM
    speed = max(0, min(100, speed))

    PWMB.duty_u16(int(speed * 65535 / 100))


def stop():
    left_motor(0)
    right_motor(0)


def forward(speed=NORMAL_SPEED):
    left_motor(speed)
    right_motor(speed)


def backward(speed=45):
    left_motor(-speed)
    right_motor(-speed)


def turn_left(speed=TURN_SPEED):
    left_motor(-speed)
    right_motor(speed)


def turn_right(speed=TURN_SPEED):
    left_motor(speed)
    right_motor(-speed)



# Distance function
def distance_cm():
    TRIG.value(0)
    sleep_us(2)

    TRIG.value(1)
    sleep_us(10)
    TRIG.value(0)

    try:
        pulse = time_pulse_us(ECHO, 1, 30000)
    except OSError:
        return 999

    if pulse < 0:
        return 999

    return pulse / 58



# Main obstacle avoidance loop
stop()
sleep(1)

while True:
    distance = distance_cm()
    print("Distance:", distance, "cm")

    if distance < OBSTACLE_DISTANCE:
        LED.value(1)
        stop()
        sleep(0.2)

        backward(45)
        sleep(0.45)

        stop()
        sleep(0.1)

        turn_right(45)
        sleep(0.55)

        stop()
        sleep(0.1)
        

    else:
        LED.value(0)
        forward(NORMAL_SPEED)

    sleep(0.05)
