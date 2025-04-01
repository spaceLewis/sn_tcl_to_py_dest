

```python
import os

theTestDirList = []

def list_commands():
    print("Available commands:")
    print("  list    - List all test directories")
    print("  add     - Add a test directory")
    print("  remove  - Remove a test directory")
    print("  exit    - Exit the program")

def list_test_dirs():
    print("Test directories:")
    for i, dir in enumerate(theTestDirList):
        print(f"{i+1}. {dir}")

def add_test_dir():
    while True:
        dir = input("Enter a test directory: ")
        if os.path.isdir(dir):
            theTestDirList.append(dir)
            print(f"Added test directory: {dir}")
            break
        else:
            print("Invalid directory. Please enter a valid directory.")

def remove_test_dir():
    if not theTestDirList:
        print("No test directories to remove")
        return
    list_test_dirs()
    while True:
        try:
            choice = int(input("Enter the number of the test directory to remove: "))
            if choice < 1 or choice > len(theTestDirList):
                print("Invalid choice")
            else:
                dir = theTestDirList.pop(choice - 1)
                print(f"Removed test directory: {dir}")
                break
        except ValueError:
            print("Invalid choice")

def commando():
    while True:
        list_commands()
        command = input("Enter a command: ")
        if command == "list":
            try:
                list_test_dirs()
            except Exception as e:
                print(f"Error: {str(e)}")
        elif command == "add":
            add_test_dir()
        elif command == "remove":
            remove_test_dir()
        elif command == "exit":
            break
        else:
            print("Unknown command")

if __name__ == "__main__":
    commando()
```