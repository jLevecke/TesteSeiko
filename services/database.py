import pyodbc

SERVER = 'expcliente.postgresql.dbaas.com.br' 
DATABASE = 'expcliente' 
USERNAME = 'expcliente' 
PASSWORD = 'Seiko@2805' 
connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
conn = pyodbc.connect(connectionString)
