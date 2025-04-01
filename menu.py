

```python
import sys

class Menu:
    def __init__(self):
        self.layers = {
            'main': {
                'options': ['Run tests', 'Load libraries', 'Display help', 'Quit', 'Reload menu'],
                'actions': [self.run_tests, self.load_libraries, self.display_help, self.quit, self.reload_menu]
            }
        }
        self.current_layer = 'main'

    def display_menu(self):
        print(f"\n--- {self.current_layer.capitalize()} Menu ---")
        for i, option in enumerate(self.layers[self.current_layer]['options'], start=1):
            print(f"{i}. {option}")

    def get_user_input(self):
        while True:
            try:
                choice = int(input("\nEnter your choice: "))
                if 1 <= choice <= len(self.layers[self.current_layer]['options']):
                    return choice
                else:
                    print("Invalid choice. Please choose a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def execute_action(self, choice):
        action = self.layers[self.current_layer]['actions'][choice - 1]
        action()

    def run_tests(self):
        print("Running tests...")

    def load_libraries(self):
        print("Loading libraries...")

    def display_help(self):
        print("Displaying help...")

    def quit(self):
        print("Quitting application...")
        sys.exit(0)

    def reload_menu(self):
        print("Reloading menu...")

    def main_layer(self):
        while True:
            self.display_menu()
            choice = self.get_user_input()
            if choice == len(self.layers[self.current_layer]['options']):
                if self.layers[self.current_layer]['options'][choice - 1] == 'Quit':
                    self.quit()
                elif self.layers[self.current_layer]['options'][choice - 1] == 'Reload menu':
                    self.reload_menu()
            else:
                self.execute_action(choice)

if __name__ == "__main__":
    menu = Menu()
    menu.main_layer()
```