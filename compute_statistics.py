"""Module providing a function printing python version."""
import sys
import time
import re
import os
from collections import Counter

def read_file(file_path):
    """Function opening a txt file."""
    try:
        with open(file_path, encoding="utf-8") as file:
            lines = file.readlines()
            # Extract numbers
            key = r'-?\d+(?:[,.]\d+)?'
            fil = [line for line in lines if ';' not in line]
            replaced = [value.replace(',', '.') for line in fil for value in re.findall(key, line)]
            data = [float(value) for value in replaced]
            return data, len(lines)
    except FileNotFoundError:

        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    except ValueError:
        print("Error: Invalid value")
        sys.exit(1)
    except ImportError as e:
        print(f"Error: File cannot be open: {e}")
        sys.exit(1)

def compute_mean(data):
    """Calculate mean."""
    return round( sum(data) / len(data), 7)

def compute_median(data):
    """Calculate median."""
    sorted_data = sorted(data)
    n = len(data)
    middle = n // 2

    if n % 2 == 0:
        return round((sorted_data[middle - 1] + sorted_data[middle]) / 2, 7)
    else:
        return round (sorted_data[middle], 2)

def compute_mode(data):
    """Calculate mode"""
    counter = Counter(data)
    max_frequency = max(counter.values())
    mode_values = [key for key, value in counter.items() if value == max_frequency]
    if len(mode_values) > 20:
        return "N/A"
    else:
        return mode_values

def compute_standard_deviation(data, mean):
    """Calculate Standard Desviation."""
    return round((sum((x - mean) ** 2 for x in data) / (len(data))) ** 0.5, 7)

def compute_variance(data, mean):
    """Calculate Variance."""
    return round(sum((x - mean) ** 2 for x in data) / (len(data)-1), 5)

def main():
    """Main"""
    if len(sys.argv) != 2:
        print("Usage: python compute_statistics.py fileWithData.txt")
        sys.exit(1)

    file_name = sys.argv[1]
    start_time = time.time()

    # Obtain the full path to the file fileWithData.txt in the current directory
    file_path = os.path.join(os.getcwd(), file_name)

    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"Error: File '{file_name}' not found.")
        sys.exit(1)

    # Obtain numeric data, the count of numeric elements, and the total line count
    data, total = read_file(file_path)
    mean = round(sum(data) / len(data), 7) if data else None
    median = round(compute_median(data), 7) if data else None
    # Compute a single mode
    mode = round(compute_mode(data)[0], 7) if compute_mode(data)!= "N/A"  else "#N/A"
    variance = round(compute_variance(data, mean), 7) if data else None
    std_deviation = round(compute_standard_deviation(data, mean), 7) if data else None

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Print results on the screen
    print(f"COUNT: {total}")
    print(f"MEAN: {mean}")
    print(f"MEDIAN: {median}")
    print(f"MODE: {mode}")
    print(f"SD: {std_deviation}")
    print(f"VARIANCE: {variance}")
    print(f"ELAPSED TIME: {elapsed_time} seconds")

    # Save results to the specified output file
    with open('StatisticsResults.txt', 'w', encoding="utf-8") as results_file:
        results_file.write(f"COUNT: {total}\n")
        results_file.write(f"MEAN: {mean}\n")
        results_file.write(f"MEDIAN: {median}\n")
        results_file.write(f"MODE: {mode}\n")
        results_file.write(f"SD: {std_deviation}\n")
        results_file.write(f"VARIANCE: {variance}\n")
        results_file.write(f"ELAPSED TIME: {elapsed_time} seconds\n")

if __name__ == "__main__":
    main()
    # End-of-file
    