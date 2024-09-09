import pyodbc

SERVER = 'clientexp.mysql.dbaas.com.br' 
DATABASE = 'clientexp' 
USERNAME = 'clientexp' 
PASSWORD = 'Seiko@2805' 
connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
conn = pyodbc.connect(connectionString)
