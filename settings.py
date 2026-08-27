from pybricks.parameters import Direction, Port

# Set to true only if/when needed
# Note: Drive base motors are assumed to exist
ARM1_MOTOR_EXISTS = True
ARM2_MOTOR_EXISTS = True
RIGHT_COLOR_SENSOR_EXISTS = False
LEFT_COLOR_SENSOR_EXISTS = False
ULTRASONIC_SENSOR_EXISTS = False
FORCE_SENSOR_EXISTS = False

# Use the Gyro to assist navigation
USE_GYRO = True

# Small SPIKE wheel: 56 mm
# Large SPIKE wheel: 88 mm
WHEEL_DIAMETER = 88

# Axle Track is the separation in mm between the centerlines
# of the right and left wheels of the drive base
AXLE_TRACK = 143

# Motor Ports
RIGHT_MOTOR_PORT = Port.E
LEFT_MOTOR_PORT = Port.A
ARM1_PORT = Port.B
ARM2_PORT = Port.F

# Sensor Ports
RIGHT_COLOR_SENSOR_PORT = Port.B
LEFT_COLOR_SENSOR_PORT = Port.A
FORCE_SENSOR_PORT = Port.A
ULTRASONIC_SENSOR_PORT = Port.B

# Motor Directions
RIGHT_MOTOR_DIRECTION = Direction.CLOCKWISE # Direction that makes this wheel drive the robot forward
LEFT_MOTOR_DIRECTION = Direction.COUNTERCLOCKWISE # Reversed from Right motor if the mounting is mirrored
ARM1_MOTOR_DIRECTION = Direction.CLOCKWISE
ARM2_MOTOR_DIRECTION = Direction.CLOCKWISE

# General defaults
MIN_BATTERY_VOLTAGE = 7500
DEFAULT_STRAIGHT_SPEED = 300
DEFAULT_STRAIGHT_ACCELERATION = 200
DEFAULT_TURN_SPEED = 200
DEFAULT_TURN_ACCELERATION = 200
