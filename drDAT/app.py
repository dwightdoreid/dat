#!/usr/bin/python
import subprocess
from flask import Flask, render_template, send_from_directory
from analyses.test1 import test1
from analyses.HelloWorld import HelloWorld

app = Flask(__name__)

##Utility Functions
#########################################################################################################

@app.route('/')
def hello_world():
   return render_template('home.html')

@app.route('/img/<path:filename>') 
def send_file(filename): 
    return send_from_directory('.', filename)


##Analyses Functions
#########################################################################################################
@app.route('/test1')
def analysis_test1():
   return test1.test1()

@app.route('/HelloWorld')
def analysis_HelloWorld():
   return HelloWorld.HelloWorld()

if __name__ == '__main__':
   app.run(debug = True)
