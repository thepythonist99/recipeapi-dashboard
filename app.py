"""
File to create an instance of the FastAPI class
"""

import urllib3

from flask import Flask


# instantiate a flask app
app = Flask(__name__)

# mount the static directory to the FastAPI app
#app.mount("/static", StaticFiles(directory="static"), name="static")

# templates instance for displaying coverage report
#templates = Jinja2Templates(directory="templates")

# Creating a PoolManager instance for sending requests.
http = urllib3.PoolManager()
