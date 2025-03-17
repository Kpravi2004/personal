import csv
import random
import pandas as pd

def load_csv(filename):
    """Loads the CSV file and returns a DataFrame."""
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Period", "Winning Result", "Bet Amount Red", "Bet Amount Green", "Bet Amount Blue", "Prediction"])

def save_csv(df, filename):
    """Saves the DataFrame to a CSV file."""
    df.to_csv(filename, index=False)

def predict_next_winner(df):
    """Predicts the next winning result based on past data."""
    if df.empty:
        return random.choice(["Red", "Green", "Blue"])  # Random for first round
    
    last_winner = df.iloc[-1]['Winning Result']
    return random.choice(["Red", "Green", "Blue"])  # Change this to a real prediction model

def add_new_result(filename, period, winner, bet_red, bet_green, bet_blue):
    """Adds a new result to the CSV file and predicts the next round."""
    df = load_csv(filename)
    prediction = predict_next_winner(df)
    
    new_data = pd.DataFrame({
        "Period": [period],
        "Winning Result": [winner],
        "Bet Amount Red": [bet_red],
        "Bet Amount Green": [bet_green],
        "Bet Amount Blue": [bet_blue],
        "Prediction": [prediction]
    })
    
    df = pd.concat([df, new_data], ignore_index=True)
    save_csv(df, filename)
    return prediction

# Example usage:
csv_file = "betting_results.csv"
print("Enter the new round details:")
period = input("Period Number: ")
winner = input("Winning Result (Red/Green/Blue): ")
bet_red = float(input("Bet Amount on Red: "))
bet_green = float(input("Bet Amount on Green: "))
bet_blue = float(input("Bet Amount on Blue: "))

predicted_next = add_new_result(csv_file, period, winner, bet_red, bet_green, bet_blue)
print(f"Predicted Next Winning Result: {predicted_next}")
