from split_settings.tools import include
from dotenv import load_dotenv
import os

load_dotenv()


include('base.py')

if 'development' in os.environ.get('mode'):
    include('development.py')
elif 'production' in os.environ.get('mode'):
    include('production.py')

