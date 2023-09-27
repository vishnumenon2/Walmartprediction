from flask import Flask,render_template,request
import pandas as pd
import pickle

with open('walmartmodel.pkl', 'rb') as model_file:
    pickle_file = pickle.load(model_file)

model = pickle_file['model']
scaler = pickle_file['scalar']

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict',methods=["POST"])
def predict():
    text=request.form["store"]
    text1=request.form["holiday"]
    text2=request.form["temperature"]
    text3=request.form["fuelprice"]
    text4=request.form["cpi"]   
    text5=request.form["unemployment"]    
    text6=request.form["week"]
    text7=request.form["weekday"]

    new_data = [[text, text1, text2, text3,text4, text5,text6, text7]]
    
    columns = ['Store', 'Holiday_Flag','Temperature','Fuel_Price', 'CPI',  'Unemployment', 'Week','WeekDay']

    new_df = pd.DataFrame(new_data, columns=columns)

    scld = scaler.transform(new_df)
    return  render_template('index.html', result=str(model.predict(scld)))


# if __name__=="__main__":
#     app.run(debug=True)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)