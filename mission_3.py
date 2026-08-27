"""
Add a description of the mission here...
"""
from pybricks.tools import multitask, run_task
from robot_config import *

async def main():

    # Set up the mission
    setup_mission()

    # drive to destination via arc to save time
    await robot.straight(200)
    await robot.curve(radius=300, angle=90)

    #return to base
    await robot.curve(radius=-300, angle=90)
    await robot.straight(-200)

    # Clean up the mission
    cleanup_mission()

if __name__ == "__main__":
    run_task(main())