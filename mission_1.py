"""
Add a description of the mission here...
"""
from pybricks.tools import multitask, run_task
from robot_config import *

async def main():

    # Set up the mission
    setup_mission()
    
    # Set custom slow straight and turn speeds
    robot.settings(straight_speed=100) 
    robot.settings(turn_rate=50)

    # Navigate to the target slowly
    await robot.straight(230)
    await robot.turn(90)
    await robot.straight(150)
    
    # Run the attachment arm slowly
    await arm2.run_angle(100,180)

    # Set custom straight and turn speeds and accelerations
    robot.settings(straight_speed=900)
    robot.settings(turn_rate=900)
    robot.settings(straight_acceleration=900)
    robot.settings(turn_acceleration=900)

    # Return to base
    await robot.straight(-150)
    await robot.turn(-90)
    await robot.straight(-230)

    # Clean up the mission
    cleanup_mission()

if __name__ == "__main__":
    run_task(main())