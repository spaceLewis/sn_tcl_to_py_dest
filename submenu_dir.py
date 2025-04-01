

```python
import os

theTestSubDirList = []

def get_test_subdirectories():
    global theTestSubDirList
    try:
        theTestSubDirList = [name for name in os.listdir('.') if os.path.isdir(name)]
    except OSError as e:
        print(f"Error: {e.filename} - {e.strerror}.")
        return []

def print_menu():
    if not theTestSubDirList:
        print("No test directories found.")
        return
    print("Main Menu:")
    for i, dir in enumerate(theTestSubDirList):
        print(f"{i+1}. {dir}")

def get_user_input():
    while True:
        try:
            choice = int(input("Enter the number of your chosen test directory: "))
            if 1 <= choice <= len(theTestSubDirList):
                return theTestSubDirList[choice - 1]
            else:
                print("Invalid choice. Please enter a number within the range.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def submenu_dir():
    get_test_subdirectories()
    print_menu()
    if not theTestSubDirList:
        return None
    return get_user_input()

if __name__ == "__main__":
    selected_dir = submenu_dir()
    if selected_dir:
        print(f"Selected test directory: {selected_dir}")
```