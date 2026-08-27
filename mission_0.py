"""
Add a description of the mission here...
"""
from pybricks.tools import multitask, run_task
from robot_config import *

async def main():

    # Set up the mission
    setup_mission()

    # Drive to target
    await robot.straight(300)
    await robot.turn(90)
    await robot.straight(50)

    # Move attachment arms
    await arm1.run_angle(500,360)
    await arm2.run_angle(500,360)
    
    # Return to base
    await robot.straight(-50)
    await robot.turn(-90)
    await robot.straight(-300)

    # Clean up the mission
    cleanup_mission()

if __name__ == "__main__":
    run_task(main())
