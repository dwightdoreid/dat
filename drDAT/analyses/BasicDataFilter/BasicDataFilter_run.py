import os
import numpy as np
import pandas as pd
from datetime import datetime
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'dataFiles'
appPort = 5100

@app.route('/f/<path:filename>') 
def send_file(filename): 
    return send_from_directory('.', filename)


@app.route('/BasicDataFilter', methods = ['POST', 'GET'])
def BasicStatistics_hello():
    if request.method == 'POST':
        f = request.files['myFile']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        return receiveData(f.filename)
        #return "<h2>file uploaded successfully</h2>"
        # result = request.form
        # return result
    return "<h1>Something Went Wrong! No filtering Done</h1>"
#///////////////////////////////////////////////////////////////////////////////////////////////////////// 
@app.route('/filterData', methods = ['POST', 'GET'])
def filterData():    
    dataFileName = str(request.form['dfname'])
    data = pd.read_csv("dataFiles/"+dataFileName)
    
    try:
        row = str(request.form['row'])
    except:
        row = None

    col = str(request.form['col'])   
    
    if (not row is None):
        res = data.loc[data[col]==row]
    else:
        res = data[[col]]
    
    tme = str(datetime.now())
    tme = tme.replace(':','_')
    tme = tme.replace(' ','_')
    tme = tme.replace('-','_')
    tme = tme.replace('.','_')
    #res.to_csv(path_or_buf = "tempFiles/red"+tme+".csv", index=False)
    res.to_csv(path_or_buf = "red.csv", index=False)
    webStrng = res.to_html(max_rows=None, classes=["table", "table-striped", "table-hover", "thead-dark"])
    return webStrng
#///////////////////////////////////////////////////////////////////////////////////////////////////////// 
@app.route('/getUniqueRows', methods = ['POST', 'GET'])
def getUniqueRows():    
    dataFileName = str(request.form['dfname'])
    data = pd.read_csv("dataFiles/"+dataFileName)
    uniqueRowEntries = data.drop_duplicates(subset=str(request.form['col']))
    webStrng = redList2Select(list(uniqueRowEntries[str(request.form['col'])]), "unique_rows")
    return webStrng
#///////////////////////////////////////////////////////////////////////////////////////////////////////// 

#///////////////////////////////////////////////////////////////////////////////////////////////////////// 

def receiveData(dataFileName):
    #redInfo = " "

    data = pd.read_csv("dataFiles/"+dataFileName)
    # data_top = data.head()
    # data_columns = ",".join(list(data.columns))
    data_columns_html = redList2Select(list(data.columns), "data_columns")
    data_rows_html = "<div id='data_rows_div'></div>"
    # data_rows_html = redList2Select(list(data.drop_duplicates()), "data_rows")
    # data_rows_html = data.drop_duplicates(subset="Entity").to_html()

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
            <title>BasicDataFilter</title>
            <meta name="description" content="">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />
            <meta http-equiv="Pragma" content="no-cache" />
            <meta http-equiv="Expires" content="0" />
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
        </head>
        <body onload="initLoad()">
            <nav class="navbar navbar-expand-sm bg-dark navbar-dark">
                <a class="navbar-brand" href="http://localhost:5000">Data Analysis Tool</a>
            </nav>
            <h1>Basic Filter</h1><br><br>
    """
    # webStrng = webStrng + "<form action = 'http://localhost:" + str(appPort) + "'" + """
    #     id = 'filterForm'>
    #     <input type='submit'>
    #     </form>
    # """
    webStrng = webStrng + """
        <form class="form-horizontal">
            <div class="form-group">
                <label class="control-label col-sm-2" for="data_columns">Select Data Column:</label>
                <div class="col-sm-10">
                    """ + data_columns_html + """                    
                </div>
            </div>
            <div class="form-group">
                <div class="col-sm-offset-2 col-sm-10">
                    <input type="button" onclick='dataColFilter()' value="Show This Column" class="btn btn-primary">
                </div>
            </div>
            <div class="form-group">
                <label class="control-label col-sm-2" for="unique_rows">Select Row to Update Table:</label>
                <div class="col-sm-10">
                    """ + data_rows_html + """
                </div>
            </div>
            <!--div class="form-group">
                <div class="col-sm-offset-2 col-sm-10">
                    <div class="checkbox">
                        <label><input type="checkbox"> Remember me</label>
                    </div>
                </div>
            </div-->
            <div class="form-group">
                <div class="col-sm-offset-2 col-sm-10">
                    <input type="button" onclick='dataFilterSave()' value="Save" class="btn btn-primary">
                </div>
            </div>
        </form> 


    """
    # webStrng = webStrng + data_columns_html + "<button onclick='dataColFilter()'>Click</button>"
    # webStrng = webStrng + "<div id ='saveDiv' style='border: 1px solid red'></div>"
    # webStrng = webStrng + "<button onclick='dataColFilterSave()'>Save</button>"
    # webStrng = webStrng + data_rows_html

    # webStrng = webStrng + "<button onclick='dataFilter()'>Click</button>"

    #webStrng = webStrng + data.head().to_html(max_rows=None, classes=["table", "table-striped", "table-hover", "thead-dark"])
    
    getUniqueRowsReqStrng = "col='+col+'" + "&" + "dfname=" + dataFileName 
    dataFilterReqStrng = "col='+col+'" + "&" + "row='+row+'" + "&" +  "dfname=" + dataFileName 
    dataColFilterReqStrng = "col='+col+'" + "&" + "dfname=" + dataFileName 
    # dataColFilterReqStrng = "col='+col+'" + "&" + "row=None" + "&" +  "dfname=" + dataFileName 
    

    webStrng = webStrng + """
        <div id='result'>Result</div>
        <script>
            document.getElementById('data_columns').addEventListener('change', getUniqueRows);
            
            function getUniqueRows(){
                var col =  document.getElementById('data_columns').value;
                var xhttp = new XMLHttpRequest();
                xhttp.onreadystatechange = function() {
                    if (this.readyState == 4 && this.status == 200) {
                        document.getElementById('data_rows_div').innerHTML = this.responseText;
                        document.getElementById('unique_rows').addEventListener('change', dataFilter);
                        
                    }
                };
                xhttp.open("POST", "getUniqueRows", true);
                xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
                xhttp.send('""" + getUniqueRowsReqStrng + """');                
            }
            function dataColFilter(){
                console.log('clicked');
                var col =  document.getElementById('data_columns').value;
                var row =  document.getElementById('unique_rows').value;
                var xhttp = new XMLHttpRequest();
                xhttp.onreadystatechange = function() {
                    if (this.readyState == 4 && this.status == 200) {
                        document.getElementById('result').innerHTML = this.responseText;
                        //document.getElementById('saveDiv').innerHTML = '<a href=http://localhost:5000/img/red.csv?d='+new Date().getTime()+'>Save</a>'
                        //document.getElementById('saveDiv').style.display = 'block';
                    }
                };
                xhttp.open("POST", "filterData", true);
                xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
                xhttp.send('""" + dataColFilterReqStrng + """');
            }
            function dataFilterSave(){
                window.location.href='http://localhost:5000/img/red.csv?d='+new Date().getTime();
            }
            function dataFilter(){
                var col =  document.getElementById('data_columns').value;
                var row =  document.getElementById('unique_rows').value;
                var xhttp = new XMLHttpRequest();
                xhttp.onreadystatechange = function() {
                    if (this.readyState == 4 && this.status == 200) {
                        document.getElementById('result').innerHTML = this.responseText;
                        //document.getElementById('saveDiv').innerHTML = '<a href=http://localhost:5000/img/red.csv?d='+new Date().getTime()+'>Save</a>'
                        //document.getElementById('saveDiv').style.display = 'block';
                    }
                };
                xhttp.open("POST", "filterData", true);
                xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
                xhttp.send('""" + dataFilterReqStrng + """');
            }

            function initLoad(){
                getUniqueRows();

                var x = setInterval(function(){
                    if (!document.getElementById('unique_rows')){
                        console.log("waiting");
                    }
                    else{
                        dataFilter();
                        clearInterval(x);
                    }
                }, 100);

                /*while(!document.getElementById('unique_rows')){
                    console.log("waiting");
                }*/
                
            }

        </script>
     """

    webStrng = webStrng + """       
        </body>
        </html>
    """
    
    return webStrng
#///////////////////////////////////////////////////////////////////////////////////////////////////////// 

def redList2Select(myList, listId):
    selectStrng = "<select class='form-control' id='" + listId + "'>"
    for element in myList:
        selectStrng = selectStrng + "<option value='" + str(element) + "'>" + str(element) + "</option>"
    selectStrng = selectStrng + "</select>"
    return selectStrng
#///////////////////////////////////////////////////////////////////////////////////////////////////////// 

#///////////////////////////////////////////////////////////////////////////////////////////////////////// 



if __name__ == '__main__':
    app.run(debug = True, port = appPort)