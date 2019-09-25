#!/usr/bin/python
import subprocess
import os

path = 'analyses\\'
analyses = []

# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    analyses.append(d)

print(analyses[0])

strng = """
#!/usr/bin/python
import subprocess
from flask import Flask, render_template, send_from_directory
"""
from analyses.test1 import test1
from analyses.HelloWorld import HelloWorld

for analysis in analyses[0]:
    strng = strng + "from analyses." + analysis + " import " + analysis + "\n"

strng = strng + """
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

"""
for analysis in analyses[0]:
    #print(analysis)
    strng = strng + "@app.route('/" + analysis + "')\ndef analysis_" + analysis + "():\n" + "\treturn " + analysis + "." + analysis +"()\n"


#strng = strng + "@app.route('/test1')\ndef analysis_" + "test1():\n" + "\treturn test1.test1()"

strng = strng + """
if __name__ == '__main__':
   app.run(debug = True)
"""
appFile = open("app.py", "w+")
appFile.write(strng)
appFile.close()

strng2 = """
<!DOCTYPE html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]><!-->
<html class="no-js">
<!--<![endif]-->

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title></title>
    <meta name="description" content="">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>


    <style>
        .loader {
            border: 16px solid #f3f3f3;
            border-radius: 50%;
            border-top: 16px solid #3498db;
            width: 120px;
            height: 120px;
            -webkit-animation: spin 2s linear infinite;
            /* Safari */
            animation: spin 2s linear infinite;
        }

        /* Safari */
        @-webkit-keyframes spin {
            0% {
                -webkit-transform: rotate(0deg);
            }

            100% {
                -webkit-transform: rotate(360deg);
            }
        }

        @keyframes spin {
            0% {
                transform: rotate(0deg);
            }

            100% {
                transform: rotate(360deg);
            }
        }
    </style>
</head>

<body>
    <!--[if lt IE 7]>
            <p class="browsehappy">You are using an <strong>outdated</strong> browser. Please <a href="#">upgrade your browser</a> to improve your experience.</p>
        <![endif]-->
    <nav class="navbar navbar-expand-sm bg-dark navbar-dark">
        <a class="navbar-brand" href="http://localhost:5000">Data Analysis Tool</a>
    </nav>
    <div class="container-fluid">
    <!-- <a href="http://localhost:5000/julia">Run</a> -->
    <!-- <img src="http://localhost:5000/img/images/fig.png" alt="plot"> -->
    <form>
        <h3>Select Analysis</h3>
        <select id="analyses">
"""
for analysis in analyses[0]:
    strng2 = strng2 + "\t\t\t<option>"+analysis+"</option>\n"

strng2 = strng2 + """
</select>
    </form>
    <br>
    <button type="button" onclick="runAnalysis()">Run Analysis</button>

    <div id="ldr" class="loader" style="display: none"></div>
    <div id="result"></div>
    <script async defer>
        function runAnalysis() {
            var selectedAnalysis = document.getElementById("analyses").value;
            document.getElementById("result").innerHTML = "";
            document.getElementById("ldr").style.display = "block";
            var xhttp = new XMLHttpRequest();
            xhttp.onreadystatechange = function () {
                if (this.readyState == 4 && this.status == 200) {
                    document.getElementById("ldr").style.display = "none";
                    document.getElementById("result").innerHTML =
                        this.responseText;
                }
            };
            xhttp.open("GET", "http://localhost:5000/" + selectedAnalysis, true);
            xhttp.send();
        }
    </script>
    </div>
</body>

</html>
"""

webFile = open("templates\\home.html", "w+")
webFile.write(strng2)
webFile.close()
