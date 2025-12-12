import os

def main():
    dial = list(range(0, 100))
    position = 50
    zero_counter = 0

    script_dir = os.path.dirname(os.path.abspath(__file__))

    filename = os.path.join(script_dir, "input.txt")

    print("Reading turn commands from:", filename)
    print(f"Starting Position: {position}")

    try:
        with open(filename, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return

    for turn in lines:

        direction = turn[0].upper()
        steps = int(turn[1:])

        if direction == 'L':
            turn_value = -steps
        elif direction == 'R':
            turn_value = steps

        position = (position + turn_value) % len(dial)

        if position == 0:
            zero_counter += 1
            
        print(f"{turn} -> Position: {position}")

    print(f"Hit zero {zero_counter} times.")

if __name__ == "__main__":
    main()
