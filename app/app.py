from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load('../src/claim_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""
    if request.method == 'POST':
        # Get form data
        Age = int(request.form['Age'])
        Vehicle_Age = int(request.form['Vehicle_Age'])
        Vehicle_Damage = int(request.form['Vehicle_Damage'])
        Policy_Sales_Channel = int(request.form['Policy_Sales_Channel'])
        Vintage = int(request.form['Vintage'])
        Previously_Claimed = int(request.form['Previously_Claimed'])

        input_df = pd.DataFrame([[Age, Vehicle_Age, Vehicle_Damage, Policy_Sales_Channel, Vintage, Previously_Claimed]],
                                columns=['Age','Vehicle_Age','Vehicle_Damage','Policy_Sales_Channel','Vintage','Previously_Claimed'])
        pred = model.predict(input_df)[0]
        result = "Approved" if pred==1 else "Rejected"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

