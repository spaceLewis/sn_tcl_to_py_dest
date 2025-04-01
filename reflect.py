

import sys

def reflect(input_value):
    if not isinstance(input_value, int) or input_value < 0 or input_value > 255:
        raise ValueError("Input value must be an integer between 0 and 255")
    result = 0
    for i in range(8):
        if (input_value & (1 << i)) != 0:
            result |= (1 << (7 - i))
    return result

def main():
    if len(sys.argv) != 2:
        print("Usage: python reflect.py <input_value>")
        sys.exit(1)
    try:
        input_value = int(sys.argv[1], 2)
        result = reflect(input_value)
        print(bin(result)[2:].zfill(8))
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()