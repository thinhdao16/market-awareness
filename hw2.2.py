from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route("/get_customer_info")
def get_customer_info():
    df = pd.read_csv('Telco-Customer-Churn.csv')

    filtered_df = df.nsmallest(20, 'MonthlyCharges').sort_values('MonthlyCharges', ascending=False)

    result = filtered_df.to_json(orient='records')

    return result

# Run the main
if __name__ == "__main__":
    app.run()
