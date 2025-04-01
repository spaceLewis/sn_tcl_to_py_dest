

import os

theTestSubDirList = []

def driveDisplayTestDir():
    try:
        for root, dirs, files in os.walk("."):
            for dir in dirs:
                if dir.startswith("test"):
                    theTestSubDirList.append(os.path.join(root, dir))
        for dir in theTestSubDirList:
            print(dir)
    except Exception as e:
        print(f"An error occurred: {e}")

driveDisplayTestDir()