from flask import Flask, jsonify, request, render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application

#import model
lasso_model = pickle.load(open(r'./model/lass.pkl', 'rb'))
scaler_model = pickle.load(open(r'./model/scal.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == "POST":
        Temperature = float(request.form.get('Temperature'))
        RHe = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMCe = float(request.form.get('FFMC'))
        DMCe = float(request.form.get('DMC'))
        DCe = float(request.form.get('DC'))
        ISIe = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))
        
        new_scaled_data = scaler_model.transform([[Temperature,RHe,Ws,Rain, FFMCe, DMCe,DCe, ISIe, Classes, Region]])
        result = lasso_model.predict(new_scaled_data)
      
        
        return render_template('index.html', results = result[0])
        
    else:
        return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
