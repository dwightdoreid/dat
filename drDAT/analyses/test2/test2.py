import subprocess, threading

def test2():
    strng = """
        <h2>Hello World</h2>
        <form action="http://localhost:5500/test2_hello" method = "POST" enctype = "multipart/form-data">
        Select a file: <input type="file" name="myFile"><br><br>
        <input type="submit">
        </form>
    """
    thread1 = threading.Thread(target = test_run)
    thread1.start()
    #test_run()
    return strng

def test_run():
    cmd = "python C:\\Users\\Dwight\\Documents\\Projects\\Dat\\Dev4\\analyses\\test2\\test2_run.py"
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    print(output)
    return "Done"