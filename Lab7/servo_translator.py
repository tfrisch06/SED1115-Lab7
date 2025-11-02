# Submit this file via brightspace

# You should not modify the signature (name, input, return type) of this function
def translate(angle: float) -> int:
	"""
	Converts an angle in degrees to the corresponding input
	for the duty_u16 method of the servo class

	See https://docs.micropython.org/en/latest/library/machine.PWM.html for more
	details on the duty_u16 method
	"""

	# Keep the angle within bounds
	if angle < 0:
		angle = 0
	elif angle > 180:
		angle = 180

	# Convert angle to pulse_width
	pulse_width = 500 + (2000 * angle / 180)

	# Convert pulse_width to duty_u16
	duty_u16 = int((pulse_width / 20000) * 65535)

	return duty_u16