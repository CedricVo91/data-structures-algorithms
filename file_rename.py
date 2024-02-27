import os


def rename_file(old_name, new_name, folder=""):
    try:
        old_path = os.path.join(folder, old_name)
        new_path = os.path.join(folder, new_name)

        if os.path.exists(new_path):
            print(f"{new_name} already exists. Deleting old file.")
            os.remove(new_path)
        if os.path.exists(old_path):
            os.rename(old_path, new_path)
            print(f"Renamed {old_name} to {new_name}.")
        else:
            print(f"{old_name} not found in {folder}.")
    except OSError as e:
        print(f"Error occurred: {e}")


# Usage
rename_file("importos.py", "Section4Ex1.py", "ZTM")
