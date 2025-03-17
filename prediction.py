import pandas as pd
import random

# File name for the CSV
csv_filename = "game_results.csv"

# Function to read the CSV file
def read_csv(filename):
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Period", "Result", "Winning_Number"])

# Function to predict the next result (Modify logic as needed)
def predict_next():
    return random.choice(["BIG", "SMALL"])  # Replace with a better prediction model

# Function to update the CSV file with the new result
def update_csv(filename, period, predicted, actual, number):
    df = read_csv(filename)
    new_data = pd.DataFrame({"Period": [period], "Result": [actual], "Winning_Number": [number]})
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(filename, index=False)
    print(f"Updated CSV with Period {period}, Actual Result: {actual}, Winning Number: {number}")

# Load past data
df = read_csv(csv_filename)
print("Last 5 Records:\n", df.tail())

# Predict next round
next_period = input("Enter the next period number: ")
predicted_result = predict_next()
print(f"Predicted Result for Period {next_period}: {predicted_result}")

# Get actual result after game ends
actual_result = input("Enter actual result (BIG/SMALL): ")
winning_number = input("Enter the winning number: ")

# Update CSV file
update_csv(csv_filename, next_period, predicted_result, actual_result, winning_number)
