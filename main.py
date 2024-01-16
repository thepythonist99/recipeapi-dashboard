"""
Main App file for the recipeAPI Dashboard project
"""

import os

from app import app
from security import SECRET_KEY

# import the necessary modules to launch the app
from user import *
from dashboard import *
from recipe import *


# run the Dashboard
if __name__ == "__main__":
  app.secret_key = SECRET_KEY
  app.run(
    host=os.environ.get('DASHBOARD_HOST'),
    port=int(os.environ.get('DASHBOARD_PORT')),
    debug=bool(os.environ.get('DASHBOARD_RELOAD'))
  )
