import subprocess, threading, os

def BasicStatistics():
    strng = """
        <h1>Basic Statistics</h1>
        <form action="http://localhost:5500/BasicStatistics_hello" method = "POST" enctype = "multipart/form-data">
            <div class="form-group" style="margin-top:10px;">
                <label id="fileLabel" for="myFile">Choose file  </label>
                <input type="file" name="myFile">
                <div class="mt-3">
                    <button type="submit" class="btn btn-primary">Submit</button>
                </div>
            </div>
        </form>

    """
    thread1 = threading.Thread(target = BasicStats_run)
    thread1.start()
    #test_run()
    return strng

def BasicStats_run():
    cmd = "python " + os.getcwd() + "\\analyses\\BasicStatistics\\BasicStatistics_run.py"
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    print(err)
    print(p_status)
    print(output)
    return "Done"