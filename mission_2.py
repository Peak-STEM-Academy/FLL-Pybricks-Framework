"""
Add a description of the mission here...
"""
from pybricks.tools import multitask, run_task
from robot_config import *

async def main():

    # Set up the mission
    setup_mission()

    # Multitask: Drive straight AND move arm simultaneously
    await multitask(
        robot.straight(200),
        arm1.run_angle(500,360)
    )

    # Multitask: Turn AND move arm simultaneously
    await multitask(
        robot.turn(90),
        arm2.run_angle(500,360)
    )
    
    # Reposition
    await robot.turn(-90)
    
    # Multitask: Drive back AND use both arms simultaneously
    await multitask(
        arm1.run_angle(700,400),
        arm2.run_angle(700,400),
        robot.straight(-200)
    )

    # Clean up the mission
    cleanup_mission()

if __name__ == "__main__":
    run_task(main())