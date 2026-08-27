# Import each of the required modules
from robot_config import hub
from pybricks.parameters import Button
from pybricks.tools import wait, run_task

# Import the mission modules:
# Mission files can be named whatever you want provided
# you use the "m#" alias to assign the mission number
try:
    import mission_0 as m0
    import mission_1 as m1
    import mission_2 as m2
    import mission_3 as m3
    #import mission_4 as m4
    #import mission_5 as m5
    #import mission_6 as m6
    #import mission_7 as m7
    #import mission_8 as m8
    #import mission_9 as m9
    #import mission_10 as m10
except:
    print('ERROR: One or more mission files are missing')
    hub.speaker.play_notes(['G5/4','E5/4','G5/4'],350)

# Mission limits
MIN_MISSION = 0
MAX_MISSION = 99

# Dynamically create the mission dictionary
# Looks for modules named m0, m1, m2 ... m99
missions = {}
for i in range(MIN_MISSION, MAX_MISSION + 1):
    module_name = f'm{i}'
    if module_name in globals():
        missions[i] = globals()[module_name]

# Adjust minimum and maximum mission to those available
MIN_AVAILABLE_MISSION = min(missions.keys())
MAX_AVAILABLE_MISSION = max(missions.keys())
print('Loaded the following mission files...')
print(missions)

# Helper Functions
def wait_for_release():
    """Ensure that all buttons are released before proceeding"""
    while hub.buttons.pressed():
        wait(10)

def show_mission(mission:int) -> None:
    """
    Display the mission number on the light matrix.
    if the number is betwen 0-9, use the larger char font.
    """
    if mission < 10:
        # Display a single digit number in a large font
        hub.display.char(str(mission))
    else:
        # Display a double digit number in a slim font
        hub.display.number(mission)

# Set the starting mission to the minimum mission
selected_mission = MIN_AVAILABLE_MISSION

# Loop the menu selection forever
print('Looking for button presses starting now...')
while True:

    # Display the selected mission
    show_mission(selected_mission)

    # Capture the current pressed buttons
    pressed = hub.buttons.pressed()

    # Increment mission selection when RIGHT is pressed
    if Button.RIGHT in pressed:
        print('RIGHT button detected')
        if selected_mission < MAX_AVAILABLE_MISSION:
            selected_mission += 1
        show_mission(selected_mission)
        wait_for_release()

    # Decrement mission selection when LEFT is pressed
    elif Button.LEFT in pressed:
        print('LEFT button detected')
        if selected_mission > MIN_AVAILABLE_MISSION:
            selected_mission -= 1
        show_mission(selected_mission)
        wait_for_release()

    # Run the selected mission when BLUETOOTH is pressed
    elif Button.BLUETOOTH in pressed:
        print('BLUETOOTH button detected')
        wait_for_release()
        hub.display.char('*')
        print(f'Starting mission: {selected_mission}')

        try:
            # Retrieve the mission module
            mission = missions[selected_mission]

            # Run the main() function inside the selected mission module
            run_task(mission.main())

        except Exception as e:
            print(f'Error running mission: {selected_mission}')
            print(type(e))
            print(e)

        # Mission complete
        print(f'Mission complete: {selected_mission}')

    # Slow down the loop to something manageable
    wait(50)