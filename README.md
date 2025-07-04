# ROBDD Equivalence Checker 🚀

## Overview 📖

The **ROBDD Checker** is a Python-based tool designed for analyzing and visualizing Boolean functions using Binary Decision Diagrams (BDDs) and Reduced Ordered Binary Decision Diagrams (ROBDDs). This project provides a user-friendly Graphical User Interface (GUI) to input Boolean functions, specify variable orderings, and perform equivalence checking. It visualizes BDD and ROBDD graphs and ensures efficient representation and comparison of Boolean functions, making it ideal for digital circuit design, verification, and synthesis. 🎨

## Features ✨

- **Input Handling** 📝: Enter two Boolean functions and their variable orderings via an intuitive GUI.
- **Error Handling** 🚫: Validates inputs for empty fields, unsaved functions, variable mismatches, and invalid operators.
- **Equivalence Checking** ✅: Compares two Boolean functions using truth table-based ROBDD comparison.
- **Visualization** 📊: Generates graphical representations of BDDs and ROBDDs using NetworkX and Matplotlib.
- **User-Friendly Interface** 🖥️: Includes a welcome page, input screen, and output display with options to visualize graphs and retry.
- **Optimization** ⚙️: Reduces BDDs to ROBDDs by consolidating terminal nodes and removing redundant nodes.

## Prerequisites 🛠️

To run the ROBDD Checker, ensure you have the following installed:
- Pycharm Or Visual Studio Code
- Python 3.8 or higher 🐍
- PySide6\~=6.8.1
- Matplotlib\~=3.10.0
- NetworkX\~=3.4.2

## Installation 📦

1. Clone the repository
2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python main.py
   ```

## Usage 🎮

1. **Launch the Application** 🚀: Start the program to access the welcome page.
2. **Navigate to Input Screen** ➡️: Click the "Start" button to proceed to the input screen.
3. **Enter Boolean Functions** ✍️:
   - Input two Boolean functions in the "Function 1" and "Function 2" text fields (e.g., `A&B|C`).
   - Click the "Save" button for each function to store it and generate variable orderings.
   - Select variable orderings from the combo-box (e.g., `A, B, C`).
4. **Check Equivalence** 🔍: Click "Calculate Equivalence" to compare the functions. The application checks for errors and displays messages if issues arise.
5. **View Results** 📈: If inputs are valid, the output page shows whether the functions are equivalent, with a fun SpongeBob SquarePants visual for equivalence! 🧽
6. **Visualize Graphs** 🖼️: Click "Show BDD1", "Show ROBDD1", or "Show ROBDD2" to display the respective graphs.
7. **Try Again** 🔄: Click "Try Again" to return to the input screen for new inputs.

## Test Cases 🧪

The following test cases demonstrate the application's functionality:

1. **Test Case 1**:
   - Function 1: `A&B|!C`
   - Function 2: `X&Y|Z`
   - Variable Ordering 1: `A, B, C`
   - Variable Ordering 2: `X, Y, Z`
   - Output: **False** ❌ (correct, as the functions are not equivalent).
2. **Test Case 2**:
   - Function 1: `(A & B) || !(C & D)`
   - Function 2: `(X & Y) || (!Z || !W)`
   - Variable Ordering 1: `A, B, C, D`
   - Variable Ordering 2: `X, Y, Z, W`
   - Output: **Correct** ❇️ (correct, as the functions are equivalent).

## Project Structure 🏗️

- **Parser Function** 🔧: Translates Boolean expressions into truth tables and constructs BDDs.
- **ROBDD Logic** ⚙️: Optimizes BDDs by consolidating terminal nodes and removing redundant nodes.
- **Comparison Function** 🔎: Compares two ROBDDs using truth table evaluation, respecting variable orderings.
- **Visualization** 📊: Uses NetworkX and Matplotlib to create pyramid-structured graphs with centered root nodes, blue edges for left children (0), and red edges for right children (1).

## 📷 GUI Preview
<img width="403" alt="image" src="https://github.com/user-attachments/assets/e56d9f85-e79b-4b57-94e7-15287c85db1b" />
<img width="403" alt="image" src="https://github.com/user-attachments/assets/3edbecbd-7f87-4224-b7d2-46a57da5bf3b" />

---

<img width="403" alt="image" src="https://github.com/user-attachments/assets/b87eefa6-62be-4a87-a6b9-838785f2707f" />

---

<p>
  <img width="400" alt="image" src="https://github.com/user-attachments/assets/8c8f287d-95eb-46af-aae1-48d9922c9a03" />
  <img width="400" alt="image" src="https://github.com/user-attachments/assets/1472a1b6-4330-46db-9a5f-dac5d153a1de" />
</p>



## Conclusion 🎉

The ROBDD Checker combines Boolean logic theory with practical tools, offering a robust platform for analyzing and visualizing Boolean functions. Its intuitive GUI and efficient algorithms make it suitable for educational purposes and real-world applications in digital design, verification, and automation. 🌟
