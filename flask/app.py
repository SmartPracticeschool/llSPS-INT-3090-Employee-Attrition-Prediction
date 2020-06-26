#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 20:55:36 2020

@author: sanjanasrinivasareddy
"""

import os

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import joblib

app = Flask(__name__)
model = pickle.load(open('regression.pkl', 'rb'))
sc=joblib.load(open('stdscale.save','rb'))
@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')
    #return "hello"
@app.route('/',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    #x_test=request.form["age"]
    x_test = [[int(x) for x in request.form.values()]]
    print(x_test)
    x_test=sc.transform(x_test)
    print(x_test)
    prediction = model.predict(x_test)
    print(prediction)
#    output=prediction[0][0]
#    return render_template('index.html', prediction_text='the employee stayed or no {}'.format(output))
    if(prediction==0):
        return render_template('indexx.html', prediction_text='The employee stayed')
    else:
        return render_template('indexx.html', prediction_text='The employee left')
if __name__ == "__main__":
    app.run(debug=True)