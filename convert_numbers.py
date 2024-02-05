"""Module providing a function printing python version."""
import sys
import time

def process_file(file_path):
    """Function opening a txt file."""
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            lines = file.readlines()
    except IOError as e:
        print(f"Error: {e}")
        return None

    results = []

    for index, line in enumerate(lines, start=1):
        line = line.strip()
        try:
            number = int(line)
            binary, hexadecimal = convert_to_binary_and_hex(number)
            results.append((index, number, binary, hexadecimal))
        except ValueError:
            results.append((index, line, None, None))  # None for binary and hexadecimal

    return results

def convert_to_binary_and_hex(number):
    """Function converting binary to hexadecimal."""
    binary = bin(number)[2:]
    if number < 0:
        signed_hex = hex(number & 0xFFFFFFFF)[2:]
        hexadecimal = signed_hex.upper().rjust(10, 'F')
    else:
        hexadecimal = hex(number)[2:]
    return binary, hexadecimal

def save_results_to_file(file_path, results):
    """Function saving results"""
    with open(file_path, 'w', encoding="utf-8") as result_file:
        for index, value, binary, hex_value in results:
            if binary is not None:
                result_file.write(f"{index} {value} {binary} {hex_value.upper()}\n")
            else:
                result_file.write(f"{index} {value} #VALUE! #VALUE!\n ")

def main():
    """Main function"""
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    start_time = time.time()

    results = process_file(input_file)

    if results:
        save_results_to_file("ConvertionResults.txt", results)

        for index, value, binary, hex_value in results:
            if binary is not None:
                print(f"{index} {value} {binary} {hex_value.upper()}\n")
            else:
                print(f"{index} {value} #VALUE! #VALUE!\n ")

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"\nELAPSED TIME: {elapsed_time:.4f} seconds")
    with open("ConvertionResults.txt", 'a', encoding="utf-8") as result_file:
        result_file.write(f"\nELAPSED TIME: {elapsed_time:.4f} seconds")

if __name__ == "__main__":
    main()
    # End-of-file
