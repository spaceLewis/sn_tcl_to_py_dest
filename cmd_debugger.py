

def PRINT_MESSAGE_TO_CONSOLE(message):
    if not isinstance(message, str):
        raise TypeError("Input message must be a string")
    print(message)

try:
    PRINT_MESSAGE_TO_CONSOLE('Hello, debugger!')
except Exception as e:
    print(f"An error occurred: {e}")