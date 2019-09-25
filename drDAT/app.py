
#!/usr/bin/python
import subprocess
from flask import Flask, render_template, send_from_directory
from analyses.BasicDataFilter import BasicDataFilter
from analyses.BasicStatistics import BasicStatistics
from analyses.HelloWorld import HelloWorld
from analyses.SysData import SysData
from analyses.test1 import test1
from analyses.test2 import test2

app = Flask(__name__)

##Utility Functions
#########################################################################################################

@app.route('/')
def hello_world():
   return render_template('home.html')

@app.route('/img/<path:filename>', methods = ['POST', 'GET']) 
def send_file(filename):
	return send_from_directory('.', filename)


##Analyses Functions
#########################################################################################################

@app.route('/BasicDataFilter')
def analysis_BasicDataFilter():
	return BasicDataFilter.BasicDataFilter()
@app.route('/BasicStatistics')
def analysis_BasicStatistics():
	return BasicStatistics.BasicStatistics()
@app.route('/HelloWorld')
def analysis_HelloWorld():
	return HelloWorld.HelloWorld()
@app.route('/SysData')
def analysis_SysData():
	return SysData.SysData()
@app.route('/test1')
def analysis_test1():
	return test1.test1()
@app.route('/test2')
def analysis_test2():
	return test2.test2()

if __name__ == '__main__':
   app.run(debug = True)
