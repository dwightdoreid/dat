
#!/usr/bin/python
import subprocess
from flask import Flask, render_template, send_from_directory
from analyses.HelloWorld import HelloWorld
from analyses.SysData import SysData
from analyses.test1 import test1

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

@app.route('/HelloWorld')
def analysis_HelloWorld():
	return HelloWorld.HelloWorld()
@app.route('/SysData')
def analysis_SysData():
	return SysData.SysData()
@app.route('/test1')
def analysis_test1():
	return test1.test1()

if __name__ == '__main__':
   app.run(debug = True)
