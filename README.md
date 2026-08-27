# FLL Python Template

A competition-ready Python framework for FIRST® LEGO® League teams using LEGO® SPIKE™ Prime and Pybricks.

This template provides a simple, student-friendly structure for organizing FLL robot code into individual missions that can be launched from a menu system. Hardware configuration and robot settings are centralized, making it easier to maintain code throughout the season.

## Features

- Mission selection menu
- Separate files for each mission
- Centralized robot configuration
- Team-specific settings file
- Easy to customize for any FLL robot design
- Designed for students learning Python

## Included Files

| File | Purpose |
|--------|---------|
| `menu.py` | Mission selection and execution |
| `robot_config.py` | Motors, sensors, drive base, and hardware configuration |
| `settings.py` | Team and robot settings |
| `mission_0.py` | Example mission |
| `mission_1.py` | Example mission |
| `mission_2.py` | Example mission |
| `mission_3.py` | Example mission |

## Philosophy

This template is intended to give FLL teams a clean starting point for developing competition code. Each mission is kept in its own file, making it easier for students to develop, test, and maintain missions independently while sharing a common robot configuration.  Mission files can be named and run individually during development and then added to the menu system when the missions sequence is ready to be integrated.

## Getting Started

1. Download or clone this repository.
2. Install Pybricks on your SPIKE Prime hub.
3. Adjust robot specific settings in `settings.py`.
4. Create or modify mission files as needed.
5. Run mission files individually during development.
6. Adjust `menu.py` with a mapping of mission filenames to mission number.
7. Run `menu.py` and select missions for testing or competition.

## Customization

Every FLL team is different. This template is designed to be modified to fit your team's robot design, programming style, and competition strategy. Add missions, helper functions, sensors, and attachments as your robot evolves throughout the season.

## Acknowledgements

This template is derived from concepts and code organization originally developed by the Snowbotics FLL Team (Team 39131). Their willingness to share resources with the FLL community made this project possible. Please consider visiting and supporting their repositories:

- https://github.com/Snowbotics39131
- https://github.com/Snowbotics39131/FLL-Pre-Season-Code

Thank you to the Snowbotics students, mentors, and families for helping advance Python programming within FIRST LEGO League.

## Disclaimer

This project is an independent community resource and is not affiliated with or endorsed by FIRST®, LEGO®, LEGO Education, Pybricks, or FIRST® LEGO® League.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.