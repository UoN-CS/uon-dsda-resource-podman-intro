import numpy as np

def load_numbers(file_path):
    with open(file_path, 'r') as file:
        numbers = [float(line.strip()) for line in file]
    return numbers

def calculate_mean(numbers):
    return np.mean(numbers)

if __name__ == "__main__":
    file_path = 'data/numbers.txt'  # Replace with your file path
    numbers = load_numbers(file_path)
    mean = calculate_mean(numbers)
    print(f"The mean of the numbers is: {mean}")

    with open('results.txt', 'w') as result_file:
        result_file.write(f"{mean}\n")

