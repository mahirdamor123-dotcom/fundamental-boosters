# Interactive Personal Data Collector

A simple beginner Python program based on the **Fundamental Booster** assignment. The program asks for a name, age, height, and favourite number. It demonstrates variables, data types, `input()`, `print()`, type conversion, arithmetic operators, `type()`, and `id()` in a straightforward top-to-bottom script.

## Requirements

- Python 3.10 or newer
- No additional packages

## Run

Open a terminal in this folder and run:

```powershell
python main.py
```

If Windows does not recognize `python`, try:

```powershell
py main.py
```

## What it does

1. Collects the user's name (`str`), age (`int`), height in meters (`float`), and favourite number (`int`).
2. Calculates an approximate birth year, age next year, and twice the favourite number.
3. Converts height from `float` to `int` and age from `int` to `str`.
4. Displays each original variable's value, type, and runtime `id()`.

## Assumptions

- Age and favourite number are entered as whole numbers; height is entered as a decimal number in meters.
- Birth year is estimated as the current year minus age; the program does not check whether the user's birthday has occurred this year.
- `int(height)` truncates the decimal part, while `round(height)` rounds the value.
- `id()` is only a runtime identity value and can change each time the program runs.
- Answers are not saved or sent anywhere. Avoid entering sensitive personal information.

## Files

```text
main.py       Program source
README.md     Setup and explanation
