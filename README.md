create by Behnam Mehdi Poor


The code starts by importing necessary libraries/modules such as pandas, Flask, mysql.connector, BeautifulSoup, and csv.
HTML Writing Functions:

write_to_html: Writes HTML content to a file ("templates/Table2.html") based on provided lists (c_list, a_list, ti_list, u_list, ta_list).
isorepublics: Defines a function to create a table named "isorepublic" in a MySQL database with specific columns.
add: Inserts data into the "isorepublic" table in the MySQL database.
shows: Executes a SQL query to select all rows from the "isorepublic" table.
Database Setup:

Attempts to connect to a MySQL database and creates a database named "sss" if it doesn't exist.
Connects to the "sss" database.
List Processing:

Initializes empty lists (list_not_reapeat_c, list_not_reapeat_a, etc.).
Attempts to create the "isorepublic" table in the database (handled by the isorepublics function).
Reads data from a CSV file ("inform.csv") and populates the lists with the data.
HTML File Writing:

Calls write_to_html to generate and append HTML content to "templates/Table2.html" based on the data from the CSV file.
Pandas Operations:

Reads the CSV file using pandas and converts it to an HTML file ("templates/Table.html").
Flask Web Application:

Defines a Flask web application.
Creates a route ("/") that renders the "table2.html" template.
Running the Flask App:

Checks if the script is the main program and then runs the Flask application.
Notes:
The code interacts with a MySQL database to create a table and insert data.
Data is read from a CSV file ("inform.csv").
HTML files ("templates/Table2.html" and "templates/Table.html") are generated based on the data.
The Flask application provides a web interface to view the generated HTML content.
Make sure to configure the MySQL connection details, and consider securing sensitive information before deploying the code in a production environment.
