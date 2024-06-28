import os;
from dotenv import load_dotenv

load_dotenv()

PORT:int = os.getenv('PORT')
DB_URL:str = os.getenv('DATABASE_URL') 
PROJECT_NAME:str = os.getenv('PROJECT_NAME')
