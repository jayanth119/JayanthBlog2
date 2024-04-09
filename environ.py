from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.environ.get('SECRET_KEY' , "your secret key here")
DEBUG = os.environ.get('DEBUG'  , True  ) 