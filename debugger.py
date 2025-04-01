

import sys
import traceback
import os

class Debugger:
    def __init__(self):
        self.breakpoints = {}

    def set_breakpoint(self, filename, line):
        if not os.path.isfile(filename):
            print(f"Error: File '{filename}' does not exist.")
            return
        if not filename.endswith('.py'):
            print(f"Error: File '{filename}' is not a Python file.")
            return
        try:
            line = int(line)
            if line <= 0:
                print(f"Error: Invalid line number '{line}'.")
                return
        except ValueError:
            print(f"Error: Invalid line number '{line}'.")
            return
        self.breakpoints[(filename, line)] = True

    def remove_breakpoint(self, filename, line):
        if (filename, line) in self.breakpoints:
            del self.breakpoints[(filename, line)]

    def step(self, frame):
        if frame.f_code.co_filename in [f for f, _ in self.breakpoints.keys()] and frame.f_lineno in [l for _, l in self.breakpoints.keys()]:
            return self.trace
        return None

    def trace(self, frame, event, arg):
        if event == 'line':
            print(f"Line {frame.f_lineno} in {frame.f_code.co_filename}")
            if (frame.f_code.co_filename, frame.f_lineno) in self.breakpoints:
                print("Breakpoint hit!")
                sys.stdout.write(">>> ")
                sys.stdout.flush()
                command = input()
                if command == 'c':
                    return self.step
                elif command == 'n':
                    return self.trace
                elif command == 's':
                    return self.step
                elif command == 'r':
                    return None
                elif command == 'q':
                    raise SystemExit
                else:
                    print("Error: Invalid command.")
        return self.trace

    def run(self, code):
        try:
            exec(code, {})
        except Exception as e:
            traceback.print_exc()

def main():
    debugger = Debugger()
    debugger.set_breakpoint('example.py', 5)
    if os.path.isfile('example.py'):
        debugger.run(open('example.py').read())
    else:
        print("Error: File 'example.py' does not exist.")

if __name__ == '__main__':
    main()