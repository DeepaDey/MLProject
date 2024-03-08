import os
import sys
from src.MLProject.exception import CustomException
from src.MLProject.logger import logging
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv('db')


def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        pass
    except Exception as e:
        raise CustomException()
    