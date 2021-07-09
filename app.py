# import required libraries
from flask import Flask,render_template,request
import requests
import joblib
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

# Create a flask object
app = Flask("optimasation_engine")

# load the model using the joblib
model = joblib.load("final_OAPE.pkl")

# define the route(basically url) to which we need to send request
@app.route("/",methods=["GET"])
def home():
    return render_template('index.html')

sc = StandardScaler()

# define the route for post method
# http post method
@app.route('/predict',methods = ['POST'])
def predict():
        N = int(request.form['N'])

        P = int(request.form['P'])

        K = int(request.form["K"])

        temperature = int(request.form['temperature'])

        humidity = int(request.form['humidity'])

        ph = int(request.form['ph'])

        rainfall = int(request.form['rainfall'])

        output = model.predict([[N,P,K,temperature,humidity,ph,rainfall]])
        output_new = output[0]
        return render_template('index.html',prediction_text = '{} is siutable for Your soil'.format(str(output_new)))
if __name__ == '__main__':
    app.run(debug=True)