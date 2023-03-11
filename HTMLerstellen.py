#Purpose : Takes a csv and sends an email in html table format
#usage : python pycsvtotabletomail.py mytable.csv

import pandas as pd
import sys


def htmlausgabe(csvfile,name):

  df=pd.read_csv(csvfile)

  htmltable=df.to_html(index=False)
  htmltable=htmltable.replace('border="1"','border="1" style="border-collapse:collapse"')

  emailheader='<p style="font-family:Calibri,Arial"><center><h1>B&uuml;cherliste und das Ranking von '+name[:-4]+'</h1>'

  htmlheader='''<html>
  <head>
  <style>
  table.dataframe {
    border: 1px solid #1C6EA4;
    background-color: #EEEEEE;
    text-align: left;
    border-collapse: collapse;
  }
  table.dataframe td, table.dataframe th {
    border: 1px solid #AAAAAA;
    padding: 3px 2px;
  }
  table.dataframe tbody td {
    font-size: 13px;
  }
  table.dataframe tr:nth-child(even) {
    background: #D0E4F5;
  }
  table.dataframe thead {
    background: #1C6EA4;
    background: -moz-linear-gradient(top, #5592bb 0%, #327cad 66%, #1C6EA4 100%);
    background: -webkit-linear-gradient(top, #5592bb 0%, #327cad 66%, #1C6EA4 100%);
    background: linear-gradient(to bottom, #5592bb 0%, #327cad 66%, #1C6EA4 100%);
    border-bottom: 2px solid #444444;
  }
  table.dataframe thead th {
    font-size: 15px;
    font-weight: bold;
    color: #FFFFFF;
    border-left: 2px solid #D0E4F5;
  }
  table.dataframe thead th:first-child {
    border-left: none;
  }

  table.dataframe tfoot {
    font-size: 14px;
    font-weight: bold;
    color: #FFFFFF;
    background: #D0E4F5;
    background: -moz-linear-gradient(top, #dcebf7 0%, #d4e6f6 66%, #D0E4F5 100%);
    background: -webkit-linear-gradient(top, #dcebf7 0%, #d4e6f6 66%, #D0E4F5 100%);
    background: linear-gradient(to bottom, #dcebf7 0%, #d4e6f6 66%, #D0E4F5 100%);
    border-top: 2px solid #444444;
  }
  table.dataframe tfoot td {
    font-size: 14px;
  }
  table.dataframe tfoot .links {
    text-align: right;
  }
  table.dataframe tfoot .links a{
    display: inline-block;
    background: #1C6EA4;
    color: #FFFFFF;
    padding: 2px 8px;
    border-radius: 5px;
  }
  </center>
  </p>
  </style>
  '''
  emailfinal=emailheader + htmlheader + htmltable
  pfadhtml=name[:-4]+"_Export.html"
  f = open(pfadhtml,"w")
  f.write(emailfinal)
  f.close()

