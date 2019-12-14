from os import environ, path, rename, sep, symlink, walk

steamapps_root = environ.get("STEAMAPPS_ROOT", "")
starbound_app_id = environ.get("STARBOUND_STEAM_ID", "211820")

steam_workshop_folder = path.join(steamapps_root, "workshop", "content", starbound_app_id)
starbound_mods_folder = path.join(steamapps_root, "common", "Starbound", "mods")

if path.exists(steam_workshop_folder) and path.exists(starbound_mods_folder):
    for subdir, dirs, files in walk(steam_workshop_folder):
        for file in files:
            print(f"INFO: Processing {file}")
            current_path = path.join(subdir, file)
            folder_name = subdir.split("/")[-1]
            new_mod_name = f"{folder_name}.pak"
            new_mod_path = path.join(subdir, new_mod_name)

            if not path.exists(new_mod_path):
                rename(current_path, new_mod_path)
                print(f"PASS: Renamed {file} to {new_mod_name}")
            else:
                print(f"SKIP: No need to rename {file}, target matches expected name.")

            symlink_target = path.join(starbound_mods_folder, new_mod_name)

            if not path.exists(symlink_target):
                symlink(new_mod_path, symlink_target)
                print(f"PASS: Symlink created at {symlink_target}")
            else:
                print(f"SKIP: {symlink_target} already exists in destination, skipping.")
else:
    print(f"ERROR: Invalid root or destination path. {steam_workshop_folder} {starbound_mods_folder}")
