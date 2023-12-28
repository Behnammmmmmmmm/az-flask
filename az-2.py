import pandas as pd
from flask import Flask,render_template
import mysql.connector
from bs4 import BeautifulSoup
import csv

def isorepublics():
    sql = """
        CREATE TABLE isorepublic(
        category VARCHAR(255),
        author VARCHAR(255),
        title VARCHAR(255),
        url VARCHAR(255),
        tag VARCHAR(255)
        );
            """
    b.execute(sql)
    a.commit()

def add(category, author, title, url, tag):
    b.execute(f'INSERT INTO isorepublic (category, author, title, url, tag) VALUES ("{category}","{author}","{title}","{url}","{tag}")')
    a.commit()


def shows():
    b.execute('SELECT * FROM isorepublic')
    categories = b.fetchall()
    for bbb in categories:
        print(bb)

try:
    a = mysql.connector.connect(
          host="localhost",
          user="root",
          password="behnam"
        )
    b = a.cursor()
    sql = "CREATE DATABASE sss"
    b.execute(sql)
except:
    pass
try:
    a = mysql.connector.connect(
          host="localhost",
          user="root",
          password="behnam",
          database="sss"
        )
    b = a.cursor()
except:
    pass

list_not_reapeat_c=[]
list_not_reapeat_a=[]
list_not_reapeat_ti=[]
list_not_reapeat_u=[]
list_not_reapeat_ta=[]
#print(a.database)
try:
    isorepublics()
except:
    pass
    
'''
b.execute("SHOW TABLES")

for table_name in b:
   print(table_name)
'''
file=[]
with open('inform.csv') as file_obj: 
    heading = next(file_obj) 
    reader_obj = csv.reader(file_obj) 
    for row in reader_obj:
        file.append(row)

for i in file:
    try:
        list_not_reapeat_c.append(i[0])
        list_not_reapeat_a.append(i[1])
        list_not_reapeat_ti.append(i[2])
        list_not_reapeat_u.append(i[3])
        list_not_reapeat_ta.append(i[4])
        
              
    except:
        pass


for oo in range(len(list_not_reapeat_c)):
    add(list_not_reapeat_c[oo],list_not_reapeat_a[oo],list_not_reapeat_ti[oo],list_not_reapeat_u[oo],"TAG")
    with open("templates/Table2.html","a") as ap:
        ap.write(f"""
        {list_not_reapeat_ti[oo]}
	<img src="{list_not_reapeat_u[oo]}" width="600" height="600">
	<p><strong>author = {list_not_reapeat_a[oo]}</strong></p>
	<p><strong>category ={list_not_reapeat_c[oo]}<strong></p>
	<section>
      {list_not_reapeat_ta[oo]}
                    """)

with open("templates/Table2.html","a") as ap:
    ap.write("</body></html>")

a = pd.read_csv("inform.csv")
 
a.to_html("templates/Table.html")

html_file = a.to_html()

a = pd.read_csv("inform.csv")
 
a.to_html("templates/Table.html")

html_file = a.to_html()

app=Flask(__name__)


@app.route('/')

def index():
    return render_template('Table2.html')

if __name__ =='__main__': 
    app.run(debug=True)

