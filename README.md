# starbound_steam_workshop_tools

Various tools and scripts to aid in running a Steam-based dedicated Starbound server when Workshop mods are involved.

## Usage

### add_workshop_mods.py

This script is designed to work around the issue of incorrect symlinks for workshop items.  It will ensure uniqueness and readability by renaming all *.pak files to their Steam item name, and then create a symlink in the Starbound/mods folder.

You have the choice of setting your Steamapps  and mods paths in an environment variable or hardcoding it as the default value in the script itself.

#### Dependencies

* Python3 (3.6.x or greater preferred)
* Filesystem Access to respective folders

#### Setting Environment Variables

`export STEAMAPPS_ROOT=/home/my_steam_user/Steam/steamapps`

`export STARBOUND_STEAM_ID=211820`

#### Execution

`python3 add_workshop_mods.py`
