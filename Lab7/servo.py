from machine import Pin, PWM
from time import sleep
from servo_translator import translate

# Instantiate servo
servo = PWM(Pin(0))
servo.freq(50)

# Test angles
for angle in [0, 45, 90, 135, 180]:
    duty = translate(angle) # translate the angle into the duty
    print(f"Angle: {angle}°, Duty: {duty}") # Print angle and the duty
    servo.duty_u16(duty) # Update the servo pin
    sleep(1)