# Goodreads Quotes Rainmeter Skin

[![download](https://img.shields.io/badge/download-deviantart-blue)](https://www.deviantart.com/aelek/art/Rainmeter-Goodreads-Quotes-817357253)

## Prerequisites

- Windows OS (7 and newer)
- [Rainmeter](https://www.rainmeter.net/) (version >= 4.3.1.3321)
- [Python 3](https://www.python.org/downloads/) (version >= 3.5)

## Installation

Download skin from the above link and run the installer.

Edit settings in `Settings.inc` file:

- Set `UserId` variable to your Goodreads user id and `UserName` to your Goodreads username. You can obtain these from the link to your Goodreads profile, which is formed as `goodreads.com/user/show/userid-username`.
- If your Python installation is not added to `PATH` environment variable, set `Python3Executable` variable to point to the location of python executable on your system.

Install Python package requirements by positioning into `@Resources/Python/` folder and executing `pip install -r requirements.txt`

Refresh the skin. Quote should be displayed in a couple of seconds.

Enjoy!
