"""
Author : Asif Khan M Pathan
Test Automation Framework
"""
import re
import os
from json2html import *
import json

class HtmlReport():
    def generate_report(self,f):
        # Load the file
        Data = json.loads(f.read())

        # Convert Json file to Html
        html_report = json2html.convert(Data)

        # Open/Create another file to write the converted html code
        html_file = os.path.join(os.getcwd(), './Reports/html_report.html')
        with open(html_file, "w") as file1:
            file1.write(html_report)
        f2 = open(html_file, "r")
        html_data = f2.read()

        # Making Background of row having result with "PASS" as Green
        html_data = re.sub(r'<table border="1">', '<table border="3" width=40% align="center" height="200">', html_data )

        html_data = re.sub(r'<td>PASS</td>', '<tr style="background-color:#32CD32;color:#ffffff;"><td>PASS</td>', html_data)

        # Making Background of row having result with "FAIL" as Red
        html_data = re.sub(r'<td>FAIL</td>', '<tr style="background-color:#ff0000;color:#ffffff;"><td>FAIL</td>', html_data)
        print('HTML Reporting Creating.....')

        # opening the HTMl report in write mode
        f3 = open(html_file, "w")
        html_template = """<html>
        <head>
        <title>Title</title>
        </head>
        <body>
        <h1 style="text-align: center;background-color:powderblue;">HTML Report From Json File</h1>
    
        </body>
        </html>
        """
        f3.write(html_template)
        f3.write(html_data)


    def run(self):
            file_name = os.path.join(os.getcwd(), './Reports/json_report')#input('Enter The File Name With Extension: ')
            print('***********************************************************************')
            with open(file_name, 'r') as fp:
                self.generate_report(fp)

if __name__ == "__main__":
    obj = HtmlReport()
    obj.run()