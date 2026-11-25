# Progressive-Water-
# 💧 Progressive Water Tariff Analysis

## 📌 Project Overview

The **Progressive Water Tariff Analysis** is a Python-based application designed to calculate water bills for multiple households using progressive consumption slabs.

The system calculates water charges based on consumption, fixed monthly fees, and penalties for excessive usage.

It also compares water consumption patterns among different households and identifies households with unusually high water usage.

## 🎯 Objectives

- Calculate water bills for multiple households.
- Apply progressive water tariff slabs.
- Calculate fixed monthly charges.
- Apply penalties for excessive water consumption.
- Compare water consumption across households.
- Identify excessive water usage.
- Find the highest and lowest consumption.
- Generate detailed household billing reports.

## 🚰 Water Tariff Structure

The project uses the following sample tariff rates:

| Consumption Slab | Rate per KL |
|---|---:|
| 0–10 KL | ₹5 |
| 11–20 KL | ₹8 |
| 21–30 KL | ₹12 |
| Above 30 KL | ₹15 |

### Additional Charges

| Charge Type | Amount |
|---|---:|
| Fixed Monthly Charge | ₹75 |
| Excess Usage Limit | 25 KL |
| Excess Usage Penalty | 10% of water charges |

**Note:** These are sample academic tariff rates and are not official water-board charges.

## 🚀 Features

1. Multiple household registration.
2. Household ID and name input.
3. Monthly water consumption entry.
4. Progressive slab-wise billing.
5. Fixed monthly charge calculation.
6. Excess consumption penalty calculation.
7. Household consumption comparison.
8. Excessive usage identification.
9. Highest and lowest consumption identification.
10. Detailed monthly billing reports.

## 🧮 Billing Calculation

The water bill is calculated using the following formulas:

**1. Water Charges**

The total water charge is calculated by applying the appropriate rate to each consumption slab.

**2. Fixed Charges**

```text
Fixed Charge = ₹75
```

**3. Excess Usage Penalty**

```text
Penalty = Water Charges × 10%
```

The penalty applies when consumption exceeds 25 KL.

**4. Final Water Bill**

```text
Final Bill = Water Charges
           + Fixed Charges
           + Penalty
```

## 📊 Consumption Comparison

The system compares the water consumption of different households for each month.

It identifies:

- Households consuming more than 25 KL.
- Households consuming more than 30% above the average consumption for that month.
- Highest water consumption.
- Lowest water consumption.

## 💻 Technologies Used

- Python 3
- Visual Studio Code
- Git
- GitHub

## 🐍 Python Concepts Used

- Variables and Data Types
- Arithmetic Operators
- Lists
- Dictionaries
- Conditional Statements
- For Loops
- While Loops
- Functions
- User Input and Output
- Built-in Functions (`max()` and `min()`)

## 📁 Project Structure

```text
Progressive-Water-Tariff-Analysis/
│
├── water_tariff.py
├── README.md
├── problem_statement.txt
├── objectives.txt
├── assumptions.txt
├── algorithm.txt
├── pseudocode.txt
├── flowchart.png
├── test_cases.txt
│
└── output_screenshots/
    ├── output1.png
    ├── output2.png
    └── output3.png
```

## ▶️ How to Run the Project

**Step 1:** Install Python 3 on your computer.

**Step 2:** Download or clone the GitHub repository.

**Step 3:** Open the project folder in Visual Studio Code.

**Step 4:** Open the terminal.

**Step 5:** Execute the following command:

```bash
python water_tariff.py
```

**Step 6:** Enter the number of households.

**Step 7:** Enter the number of months.

**Step 8:** Enter household details and monthly water consumption.

**Step 9:** View the calculated bills and consumption comparison report.

## 🧪 Test Cases

| Test Case | Input / Condition | Expected Result |
|---|---|---|
| TC01 | Consumption = 8 KL | Bill with first slab |
| TC02 | Consumption = 15 KL | First and second slabs applied |
| TC03 | Consumption = 25 KL | First three slabs applied |
| TC04 | Consumption = 35 KL | All four slabs applied with penalty |
| TC05 | Consumption = 0 KL | Fixed charge only |
| TC06 | Consumption = 40 KL | Excess usage warning |
| TC07 | Consumption above monthly average by 30% | High usage warning |
| TC08 | Multiple households | Household comparison report |

## 📌 Expected Output

The program displays:

- Household ID and name.
- Monthly water consumption.
- Progressive water charges.
- Fixed monthly charges.
- Excess usage penalties.
- Final water bill.
- Average household consumption.
- Excessive usage warnings.
- Highest and lowest consumption.

## 📝 Conclusion

The Progressive Water Tariff Analysis system provides a simple and efficient method for calculating water bills using Python.

It applies progressive tariff slabs, fixed charges, and penalties to calculate household water expenses.

The household comparison feature helps identify excessive water usage and encourages responsible water consumption.

This project demonstrates the practical application of fundamental Python programming concepts in a real-world water billing system.

---

**Project Name:** Progressive Water Tariff Analysis

**Subject:** Python Activity-Based Learning
name: sree hasini
section:5 
**Programming Language:** Python 3

**Project Type:** Case Study
