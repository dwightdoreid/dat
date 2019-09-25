import os
import numpy as np
import pandas as pd
from datetime import datetime
from flask import Flask, render_template, request, send_from_directory
# from werkzeug import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'dataFiles'

fontSize = 6
# imgSize = (16, 4.8)
imgSize = None

@app.route('/img/<path:filename>') 
def send_file(filename): 
    return send_from_directory('.', filename)

@app.route('/BasicStatistics_hello', methods = ['POST', 'GET'])
def BasicStatistics_hello():
    if request.method == 'POST':
        f = request.files['myFile']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        return analyseData(f.filename)
        #return "<h2>file uploaded successfully</h2>"
        # result = request.form
        # return result
    return "<h1>Hello from test 2</h1>"
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
@app.route('/BasicStatistics_filter', methods = ['POST', 'GET'])
def BasicStatistics_filter():
    redInfo = " "
    if request.method == 'POST':        
        dataFileName = str(request.form['myFile'])
        data = pd.read_csv("dataFiles/"+dataFileName)
        filtCols = str(request.form['filtCols'])
        filtCols = filtCols.replace("**"," ")
        filtCols = filtCols.strip(".")
        if (filtCols == " "):
            data = data
        else:
            data = data[filtCols.split(".")]
            #data = data[[filtCols]]
            #data = data[["Wind", "Coal"]]
            #data = data.loc[:, data.columns.isin(list(filtCols))]
        tme = str(datetime.now())
        tme = tme.replace(':','_')
        tme = tme.replace(' ','_')
        tme = tme.replace('-','_')
        tme = tme.replace('.','_')
        figName = "fig.png"
        figName_box = "fig.png"
        figName_pdf = "fig.png"
        figName_hist = "fig.png"
        try:
            linePlot = data.plot(figsize=imgSize, fontsize=fontSize)
            fig = linePlot.get_figure() 
            figName = "images/fig" + tme + ".png"
            fig.savefig(figName)
            fig.close()
        except:
            redInfo = "Line Plot Failed"

        try:
            boxPlot = data.plot.box(figsize=imgSize, fontsize=fontSize)
            fig_box = boxPlot.get_figure() 
            figName_box = "images/fig_box" + tme + ".png"
            fig_box.savefig(figName_box)
            fig.close()
        except:
            redInfo = redInfo + "  Box Plot Failed"

        try:
            pdfPlot = data.plot.kde(figsize=imgSize, fontsize=fontSize)
            fig_pdf = pdfPlot.get_figure()
            figName_pdf = "images/fig_pdf" + tme + ".png"
            fig_pdf.savefig(figName_pdf)
            fig.close()
        except:
            redInfo = redInfo + "  PDF Plot Failed"

        try:
            histPlot = data.plot.hist(figsize=imgSize, fontsize=fontSize)        
            fig_hist = histPlot.get_figure() 
            figName_hist = "images/fig_hist" + tme + ".png"
            fig_hist.savefig(figName_hist)
            fig.close()
        except:
            redInfo = redInfo + "  Hist Plot Failed"
        webStrng = ""
        #webStrng = webStrng + redList2CheckBox(list(data.columns), "data_columns_checkdiv")
        webStrng = webStrng + data.describe().to_html(max_rows=None, classes=["table", "table-striped", "table-hover", "thead-dark"])
        
        #figName = "images/fig.png"
        webStrng = webStrng + "<img src='http://localhost:5000/img/" + figName + "'></img>"
        webStrng = webStrng + "<img src='http://localhost:5000/img/" + figName_box + "'></img>"
        webStrng = webStrng + "<img src='http://localhost:5000/img/" + figName_pdf + "'></img>"
        webStrng = webStrng + "<img class='img-thumbnail' src='http://localhost:5000/img/" + figName_hist + "'></img>"
    
        webStrng = '<br>' + webStrng + filtCols + redInfo
        return webStrng
    return "<h1>Something Else</h1>"
#///////////////////////////////////////////////////////////////////////////////////////////////////////// 

#///////////////////////////////////////////////////////////////////////////////////////////////////////// 

def analyseData(dataFileName):
    redInfo = " "
    data = pd.read_csv("dataFiles/"+dataFileName) 
    #data = data[["Mean female height (cm) (centimeters)"]]
    # tme = str(datetime.now())
    # tme = tme.replace(':','_')
    # tme = tme.replace(' ','_')
    # tme = tme.replace('-','_')
    # tme = tme.replace('.','_')
    # figName = "fig.png"
    # figName_box = "fig.png"
    # figName_pdf = "fig.png"
    # figName_hist = "fig.png"
    # try:
    #     linePlot = data.plot(figsize=imgSize, fontsize=fontSize)
    #     fig = linePlot.get_figure() 
    #     figName = "images/fig" + tme + ".png"
    #     fig.savefig(figName)
    # except:
    #     redInfo = "Line Plot Failed"

    # try:
    #     boxPlot = data.plot.box(figsize=imgSize, fontsize=fontSize)
    #     fig_box = boxPlot.get_figure() 
    #     figName_box = "images/fig_box" + tme + ".png"
    #     fig_box.savefig(figName_box)
    # except:
    #     redInfo = redInfo + "  Box Plot Failed"

    # try:
    #     pdfPlot = data.plot.kde(figsize=imgSize, fontsize=fontSize)
    #     fig_pdf = pdfPlot.get_figure()
    #     figName_pdf = "images/fig_pdf" + tme + ".png"
    #     fig_pdf.savefig(figName_pdf)
    # except:
    #     redInfo = redInfo + "  PDF Plot Failed"

    # try:
    #     histPlot = data.plot.hist(figsize=imgSize, fontsize=fontSize)        
    #     fig_hist = histPlot.get_figure() 
    #     figName_hist = "images/fig_hist" + tme + ".png"
    #     fig_hist.savefig(figName_hist)
    # except:
    #     redInfo = redInfo + "  Hist Plot Failed"

    webStrng = """
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
        </head>
        <body onload="colFilter()">
            <nav class="navbar navbar-expand-sm bg-dark navbar-dark">
                <a class="navbar-brand" href="http://localhost:5000">Data Analysis Tool</a>
            </nav>
            <h1>Basic Statistical Results</h1><br><br>
    """
    webStrng = webStrng + redList2CheckBox(list(data.columns), "data_columns_checkdiv", dataFileName)
    webStrng = webStrng + "<div id='result'></div>"
    # webStrng = webStrng + data.describe().to_html(max_rows=None, classes=["table", "table-striped", "table-hover", "thead-dark"])
    
    # #figName = "images/fig.png"
    # webStrng = webStrng + "<img src='http://localhost:5000/img/" + figName + "'></img>"
    # webStrng = webStrng + "<img src='http://localhost:5000/img/" + figName_box + "'></img>"
    # webStrng = webStrng + "<img src='http://localhost:5000/img/" + figName_pdf + "'></img>"
    # webStrng = webStrng + "<img class='img-thumbnail' src='http://localhost:5000/img/" + figName_hist + "'></img>"
    
    
    # filts = 'Mean female height (cm) (centimeters)'
    reqStrng = "myFile=" + dataFileName# + "&filtCols=" + filts

    webStrng = webStrng + """
        <script>
            function colFilter(){
                var cols = document.getElementsByClassName('colCheck');
                var filt = ""
                for(i=0; i<cols.length; i++){
                    if (cols[i].checked == true){
                        //alert(cols[i].value);
                        x = cols[i].value.replace(" ", "**");
                        filt = filt + x + ".";
                        //filt = "Wind";
                    }
                }
                var xhttp = new XMLHttpRequest();
                xhttp.onreadystatechange = function() {
                    if (this.readyState == 4 && this.status == 200) {
                        document.getElementById('result').innerHTML = this.responseText;
                    }
                };
                xhttp.open("POST", "BasicStatistics_filter", true);
                xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
                xhttp.send('filtCols='+filt+'&"""+reqStrng+"""');            
            }
        </script>

    """
   
    webStrng = webStrng + "<h3>" + redInfo + "</h3>"
    webStrng = webStrng + """
        </body>
        </html>
    """
    #return data.describe().to_html(max_rows=None)
    return webStrng
#///////////////////////////////////////////////////////////////////////////////////////////////////////// 
def redList2CheckBox(myList, listId, dataFileName):
    # action="http://localhost:5500/BasicStatistics_filter"
    webStrng = "<div id=" + listId + ">"
    webStrng = webStrng + """
        <form class="form-check form-check-inline" method="get">
    """
    webStrng = webStrng + """
        <!--input type="text" name="myFile" style="display:block" value="
    """+dataFileName +""" "/--> """
    
    for element in myList:
        webStrng = webStrng + '<span class="m-2">'
        webStrng = webStrng + '<input class="colCheck form-check-input" type="checkbox"'
        webStrng = webStrng + ' name="' + str(element) + '"'
        webStrng = webStrng + ' id="' + str(element) +'"'
        webStrng = webStrng + ' value="' + str(element)+'" checked="true"/>'
        webStrng = webStrng + '<label class="form-check-label" for="'+ str(element) + '">' + str(element) + '</label>'
        webStrng = webStrng + '</span>'

    webStrng = webStrng + """
            <!--input type="submit" value="Refresh"-->
            <!--input type="button" onclick="colFilter()" value="Refresh"-->
        </form>
        <br><input type="button" onclick="colFilter()" value="Refresh">
    </div>
    """
    return webStrng


#///////////////////////////////////////////////////////////////////////////////////////////////////////// 

if __name__ == '__main__':
    app.run(debug = True, port = 5500)