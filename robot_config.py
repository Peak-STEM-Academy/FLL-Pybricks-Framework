"""
ROBOT CONFIGURATION
-------------------
This file defines the physical hardware of the robot and provides helper functions.
It is the central place to configure motors, sensors, and the drive base.
"""
# Required imports
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Import the user defined settings for the robot
import settings

# Conditional Imports
if settings.RIGHT_COLOR_SENSOR_EXISTS or settings.LEFT_COLOR_SENSOR_EXISTS:
    from pybricks.pupdevices import ColorSensor

if settings.ULTRASONIC_SENSOR_EXISTS:
    from pybricks.pupdevices import UltrasonicSensor

if settings.FORCE_SENSOR_EXISTS:
    from pybricks.pupdevices import ForceSensor

# ------------------------------------------------------------------
# HUB INITIALIZATION
# ------------------------------------------------------------------

# Define the hub type and specify the hub orientation
# Use "PrimeHub" for the LEGO Spike Prime hub
# (top_side=Axis.Z, front_side=Axis.Y means display facing up, front facing forward.)
hub = PrimeHub(top_side=Axis.Z, front_side=Axis.Y)

# ------------------------------------------------------------------
# DEVICE INITIALIZATION
# ------------------------------------------------------------------

try:
    # Drive motors:
    right_motor = Motor(settings.RIGHT_MOTOR_PORT, settings.RIGHT_MOTOR_DIRECTION)
    left_motor = Motor(settings.LEFT_MOTOR_PORT, settings.LEFT_MOTOR_DIRECTION)

    # Attachment motors:
    if settings.ARM1_MOTOR_EXISTS:
        arm1 = Motor(settings.ARM1_PORT, settings.ARM1_MOTOR_DIRECTION)

    if settings.ARM2_MOTOR_EXISTS:
        arm2 = Motor(settings.ARM2_PORT, settings.ARM2_MOTOR_DIRECTION)

    # Sensors:
    if settings.RIGHT_COLOR_SENSOR_EXISTS:
        right_color_sensor = ColorSensor(settings.RIGHT_COLOR_SENSOR_PORT)

    if settings.LEFT_COLOR_SENSOR_EXISTS:
        left_color_sensor = ColorSensor(settings.LEFT_COLOR_SENSOR_PORT)

    if settings.FORCE_SENSOR_EXISTS:
        force_sensor = ForceSensor(settings.FORCE_SENSOR_PORT)

    if settings.ULTRASONIC_SENSOR_EXISTS:
        distance_sensor = UltrasonicSensor(settings.ULTRASONIC_SENSOR_PORT)

except Exception as e:
    print('ERROR: One or more expected devices are not present')
    print('Adjust the robot or check your settings.py file')
    print(type(e))
    print(e)
    raise

# ------------------------------------------------------------------
# DRIVEBASE CONFIGURATION
# ------------------------------------------------------------------
# Define a DriveBase to simplify moving the robot.
robot = DriveBase(
    left_motor,
    right_motor,
    wheel_diameter=settings.WHEEL_DIAMETER,
    axle_track=settings.AXLE_TRACK
    )

# Enable the built-in gyro for straight driving and accurate turns.
# Requires the hub orientation to be set correctly.
robot.use_gyro(settings.USE_GYRO)

# ------------------------------------------------------------------
# DIAGNOSTICS: Report low battery voltage
# ------------------------------------------------------------------
voltage = hub.battery.voltage()
print(f'Battery Voltage: {voltage} mV')
if voltage < settings.MIN_BATTERY_VOLTAGE:
    print('WARNING: Battery is low! Please charge or swap.')
    hub.speaker.play_notes(['C5/4','C5/4','C5/4'],250)

# ------------------------------------------------------------------
# FUNCTIONS
# ------------------------------------------------------------------

def wait_for_button():
    """Pauses the program until a button is pressed. Great for debugging."""
    print("PAUSED: Press any button to continue...")
    while not hub.buttons.pressed():
        wait(10)
    while hub.buttons.pressed():
        wait(10)
    print("Resuming!")

def reset_robot():
    """
    Reset the robot stopping all motors and restoring
    default robot settings.
    """
    robot.stop()
    if settings.ARM1_MOTOR_EXISTS:
        arm1.stop()
    if settings.ARM2_MOTOR_EXISTS:
        arm2.stop()
    robot.reset()
    robot.settings(
        straight_speed=settings.DEFAULT_STRAIGHT_SPEED,
        straight_acceleration=settings.DEFAULT_STRAIGHT_ACCELERATION,
        turn_rate=settings.DEFAULT_TURN_SPEED,
        turn_acceleration=settings.DEFAULT_TURN_ACCELERATION
        )
    
def setup_mission():
    """Perform required actions at the beginning of a mission"""
    reset_robot()

def cleanup_mission():
    """Perform required actions at the end of a mission"""
    reset_robot()
    
async def home_arm1(speed, torque):
    """
    Home the attachment against a physical stop
    and set the current position to 0 degrees.
    """
    if settings.ARM1_MOTOR_EXISTS:
        await arm1.run_until_stalled(speed, then=Stop.COAST, duty_limit=torque)
        arm1.reset_angle(0)

async def home_arm2(speed, torque):
    """
    Home the attachment against a physical stop
    and set the current position to 0 degrees.
    """
    if settings.ARM2_MOTOR_EXISTS:
        await arm2.run_until_stalled(speed, then=Stop.COAST, duty_limit=torque)
        arm2.reset_angle(0)

# Reset the robot to set up the default parameters
reset_robot()