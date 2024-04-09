from pandas.io import sql 
import pandas as pd 
import sqlalchemy as db
from datetime import datetime, date
import pymysql

archivo = "C:/Users/Thinkpad/Desktop/DATAOPS/python/dataset/AAPL.csv"
data = pd.read_csv (archivo)


database_username = 'root'
database_password = 'Derrickrose_1'
database_ip = '127.0.0.1'
database_name = 'schemaaapl'
database_connection = db.create_engine('mysql+pymysql://{0}:{1}@{2}/{3}'.
                                                format(database_username, database_password,
                                                    database_ip, database_name))

connection = database_connection.connect()
metadata = db.MetaData()
data.to_sql('aapl_data',connection)