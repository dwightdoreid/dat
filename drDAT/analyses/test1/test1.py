#!/usr/bin/python
import subprocess


def test1():
    cmd = "C:\\Users\\Dwight\\AppData\\Local\\Julia-1.1.1\\bin\\julia.exe C:\\Users\\Dwight\\Documents\\Projects\\Dat\\Dev2\\analyses\\test1\\test1.jl"
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    return '<img src="http://localhost:5000/img/images/fig3.png" alt="plot2">'