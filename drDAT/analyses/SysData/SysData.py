import platform 

def SysData():
    strng = "<h3> System Data </h3>"
    strng = strng + "\n<h3>" + platform.platform() + "</h3>"
    strng2 = """
    <style>
    table {
    font-family: arial, sans-serif;
    border-collapse: collapse;
    width: 100%;
    }

    td, th {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
    }

    tr:nth-child(even) {
    background-color: #dddddd;
    }
    </style>
    </head>
    <body>

    <h2>HTML Table</h2>

    <table>
    <tr>
        <th>Item</th>
        <th>Parameter</th>
        <th>Value</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Analysis Name</td>
        <td>System Data Stuff</td>
    </tr>
    """
    strng2 = strng2 + "<tr>\n<td>2</td>\n<td>Platform</td>\n<td>" + platform.platform() + "</td></tr>"
    strng2 = strng2 + "<tr>\n<td>3</td>\n<td>OS</td>\n<td>" + platform.system() + "</td></tr>"
    strng2 = strng2 + "<tr>\n<td>4</td>\n<td>Release</td>\n<td>" + platform.release() + "</td></tr>"
    strng2 = strng2 + "<tr>\n<td>5</td>\n<td>Version</td>\n<td>" + platform.version() + "</td></tr>"
    strng2 = strng2 + "<tr>\n<td>6</td>\n<td>Machine</td>\n<td>" + platform.machine() + "</td></tr>"
    strng2 = strng2 + "<tr>\n<td>7</td>\n<td>Processor</td>\n<td>" + platform.processor() + "</td></tr>"
    strng2 = strng2 + "<tr>\n<td>8</td>\n<td>Node</td>\n<td>" + platform.node() + "</td></tr>"


    strng2 = strng2 + """
    </table>
    """
    return strng2