import subprocess, threading, os

def BasicDataFilter():
    strng = """
         <h1>Basic Data Filer</h1>
        <form action="http://localhost:5100/BasicDataFilter" method = "POST" enctype = "multipart/form-data">
            <div class="form-group" style="margin-top:10px;">
                <label id="fileLabel" for="myFile">Choose file  </label>
                <input type="file" name="myFile">
                <div class="mt-3">
                    <button type="submit" class="btn btn-primary">Submit</button>
                </div>
            </div>
        </form>
    """
    thread1 = threading.Thread(target = BasicDF_run)
    thread1.start()
    return strng

def BasicDF_run():
    #cmd = "python C:\\Users\\Dwight\\Documents\\Projects\\Dat\\Dev4\\analyses\\BasicDataFilter\\BasicDataFilter_run.py"
    cmd = "python " + os.getcwd() + "\\analyses\\BasicDataFilter\\BasicDataFilter_run.py"
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    print(err)
    print(p_status)
    print(output)
    return "Done"