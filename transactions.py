import pandas as pd
import random
from datetime import datetime, timedelta

# Generate 100 sample transactions
transactions = []
locations = ["Kenya", "Tanzania", "Uganda", "Nigeria", "USA"]
types = ["transfer", "withdrawal", "payment"]

for i in range(1, 101):
    transactions.append({
        "transaction_id": i,
        "user_id": random.randint(100, 110),
        "amount": random.randint(50, 100000),
        "location": random.choice(locations),
        "transaction_type": random.choice(types),
        "time": (datetime.now() - timedelta(minutes=random.randint(0, 1000))).strftime("%Y-%m-%d %H:%M:%S")
    })

df = pd.DataFrame(transactions)

# Simple fraud detection rules
def detect_fraud(tx):
    flags = []
    if tx['amount'] > 20000:
        flags.append("High Amount")
    if tx['location'] not in ["Kenya", "Tanzania", "Uganda"]:
        flags.append("Foreign Location")
    if tx['transaction_type'] == "withdrawal" and tx['amount'] > 10000:
        flags.append("Suspicious Withdrawal")
    return ", ".join(flags)

df['fraud_alert'] = df.apply(detect_fraud, axis=1)

# Save CSV for Splunk
df.to_csv("transactions.csv", index=False)
print("Sample transaction data generated! Check transactions.csv")
