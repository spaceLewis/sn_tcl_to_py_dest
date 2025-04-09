

import serial

class MainMenu:
    def __init__(self):
        self.menu_layers = {
            'main': {
                'options': ['Test Environment', 'Quit'],
                'actions': [self.test_environment, self.quit]
            },
            'test_environment': {
                'options': ['Modbus Communication', 'Back'],
                'actions': [self.modbus_communication, self.back]
            }
        }
        self.current_layer = 'main'
        self.serial_connection = serial.Serial('COM3', 9600, timeout=1)

    def print_menu(self):
        print('\n'.join(self.menu_layers[self.current_layer]['options']))

    def get_user_input(self):
        return input('Enter your choice: ')

    def execute_action(self, choice):
        if choice < len(self.menu_layers[self.current_layer]['actions']):
            self.menu_layers[self.current_layer]['actions'][choice]()
        else:
            print('Invalid choice. Please try again.')

    def test_environment(self):
        self.current_layer = 'test_environment'

    def modbus_communication(self):
        try:
            self.serial_connection.write(b'\x01\x03\x00\x00\x00\x06')
            response = self.serial_connection.read(7)
            if response:
                print('Modbus communication successful')
            else:
                print('Modbus communication failed')
        except Exception as e:
            print(f'Error: {e}')

    def back(self):
        self.current_layer = 'main'

    def quit(self):
        print('Goodbye!')
        exit()

def main():
    menu = MainMenu()
    while True:
        menu.print_menu()
        choice = menu.get_user_input()
        if choice.lower() == 'reload':
            menu.current_layer = 'main'
        elif choice.lower() == 'quit':
            menu.quit()
        else:
            try:
                choice = int(choice)
                menu.execute_action(choice)
            except ValueError:
                print('Invalid input. Please try again.')

if __name__ == '__main__':
    main()