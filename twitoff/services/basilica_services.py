
import os
from dotenv import load_dotenv
import basilica

load_dotenv()

API_KEY = os.getenv('BASILICA_API_KEY', default='OOPS')

def basilica_api_client():
    connection = basilica.Connection(API_KEY)
    return connection

    