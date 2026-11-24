
try:
    with open("input.txt", "r") as file:
        lines = file.readlines()

    count = len(lines)
    first_two = lines[:2]

    with open("output.txt", "w") as file:
        file.writelines(first_two)

    print("Total number of lines:", count)
    print("First two lines extracted successfully.")
    print("Data written to output.txt")

except FileNotFoundError:
    print("Input file not found.")
