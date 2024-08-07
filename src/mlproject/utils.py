import os
import sys
from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import pandas as pd 
from dotenv import load_dotenv
import pymysql  

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")


def read_sql_data():
    logging.info("Reading data from sql database has been started")

    try:
        mydb=pymysql.connect(
            host = 'localhost',
            user = 'root',
            password='2001',
            db = 'COLLEGE'
            )
        logging.info("connection establised with database", mydb)
        df = pd.read_sql_query("select * from students",mydb)
        print(df.head())
        print(df.shape)
        return df

    except Exception as ex:
        raise CustomException(ex,sys)