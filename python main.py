# ehima-securenet
# Author: Ehi Mercy Adams 💻✨

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

def load_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        print(f"✅ Successfully loaded data with {len(df)} rows.")
        return df
    except Exception as e:
        print("❌ Error loading CSV:", e)
        return None

def preprocess_data(df):
    required_columns = ["Source", "Destination", "Protocol", "Length"]
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}")

    # Convert categorical values to numeric codes
    df["Protocol_Code"] = df["Protocol"].astype("category").cat.codes
    df["Source_Code"] = df["Source"].astype("category").cat.codes
    df["Destination_Code"] = df["Destination"].astype("category").cat.codes

    # Create a fake "Label" column for demonstration (0 = Normal, 1 = Suspicious)
    df["Label"] = df["Protocol"].apply(lambda x: 1 if x in ["FTP", "SSH", "Telnet"] else 0)

    features = df[["Length", "Protocol_Code", "Source_Code", "Destination_Code"]]
    labels = df["Label"]

    return features, labels

def train_and_evaluate(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    model = LogisticRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print("\n🧠 Classification Report:")
    print(classification_report(y_test, predictions))

def main():
    print("👩🏾‍💻 Program created by Ehi Mercy Adams 🌟")
    filepath = "data/traffic.csv"
    df = load_csv(filepath)
    if df is None:
        return

    try:
        X, y = preprocess_data(df)
        train_and_evaluate(X, y)
    except Exception as e:
        print("❌ Error during processing:", e)

if __name__ == "__main__":
    main()