
# Basic Calculator Program

This project is a simple, command-line calculator that performs basic arithmetic operations: addition, subtraction, multiplication, and division. It provides an interactive menu for selecting an operation and supports repeated calculations. It’s built with Python and uses basic functions and loops for functionality.

## Features
- Addition, Subtraction, Multiplication, and Division operations
- User-friendly input prompts and menu
- Input validation to prevent errors from non-numeric input
- Option to perform multiple calculations without restarting the program

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/username/calculator.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd calculator
   ```
3. **Run the script:**
   Make sure Python 3 is installed. Run the script with:
   ```bash
   python calculator.py
   ```

## Usage

1. Run the script in the command line.
2. Select the desired operation by entering the corresponding number (1-4).
3. Enter two numbers to perform the calculation.
4. View the result and choose whether to perform another calculation.

### Menu Options
```
1 = Addition
2 = Subtraction
3 = Multiplication
4 = Division
```

### Input Validation
The program checks for non-numeric inputs and will prompt the user to re-enter values if invalid data is detected.

## Code Structure

### Functions

- `addition(x, y)`: Returns the sum of `x` and `y`.
- `subtraction(x, y)`: Returns the difference of `x` and `y`.
- `multiplication(x, y)`: Returns the product of `x` and `y`.
- `division(x, y)`: Returns the quotient of `x` and `y`.

### Main Loop

The program uses a `while` loop to continuously ask the user for an operation and inputs until they choose to exit.

### Error Handling

A `try-except` block ensures that invalid inputs are handled gracefully, displaying a prompt if the user enters a non-numeric value.

## Examples

1. **Addition**
   ```
   Select an operation
   1 = Addition
   2 = Subtraction
   3 = Multiplication
   4 = Division
   Enter your choice: 1
   Enter the first number: 10
   Enter the second number: 5
   Output: 10 + 5 = 15
   ```

2. **Division with invalid input**
   ```
   Select an operation
   Enter your choice: 4
   Enter the first number: 20
   Enter the second number: abc
   Output: Error: Please enter a valid number
   ```

## Contributing

Contributions are welcome! If you have suggestions, please open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
