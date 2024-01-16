"""
Security file for the recipeAPI Dashboard
"""

import os
import urllib3


# create a secret key variable
SECRET_KEY = os.environ.get('SECRET_KEY')

# function to login a user
async def login_user(username: str, password: str):
  """
  Utility function to login a user
  Args:
    username (str): The user username
    password (str): The user password
  """
  
  # get the respective endpoint url
  login_endpoint_url = "http://{0}:{1}/api/v1/token".format(
    os.environ.get('API_URL'),
    os.environ.get('API_PORT')
  )
  
  # open the register endpoint url
  response = urllib3.request(
    method="POST",
    url=login_endpoint_url,
    fields={"username": username, "password": password}
  )

  return response.json()
