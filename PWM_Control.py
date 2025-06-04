import pigpio

class PWMControl:
    def __init__(self, Throttle_PIN=12, YAW_PIN=18, PITCH_PIN=13, ROLL_PIN=19):
        # Initialize pigpio
        self.pi = pigpio.pi()

        # Define GPIO pins for KK board connections
        self.THROTTLE_PIN = Throttle_PIN
        self.YAW_PIN = YAW_PIN
        self.PITCH_PIN = PITCH_PIN
        self.ROLL_PIN = ROLL_PIN

        # Set PWM frequency
        self.PWM_FREQUENCY = 1000
        self.pi = pigpio.pi()

    # Set PWM frequency
    PWM_FREQUENCY = 1000

    def set_pwm(self, pin, pulse_width):
        self.pi.set_servo_pulsewidth(pin, pulse_width)

    def throttle(self, value):
        pulse_width = max(1000, min(2000, value))
        self.set_pwm(self.THROTTLE_PIN, pulse_width)

    def yaw(self, value):
        pulse_width = max(1000, min(2000, value))
        self.set_pwm(self.YAW_PIN, pulse_width)

    def pitch(self, value):
        pulse_width = max(1000, min(2000, value))
        self.set_pwm(self.PITCH_PIN, pulse_width)

    def roll(self, value):
        pulse_width = max(1000, min(2000, value))
        self.set_pwm(self.ROLL_PIN, pulse_width)
