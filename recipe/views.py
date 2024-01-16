"""
Views for the recipe module
"""

import os
import urllib3

from flask import request
from flask import session
from flask import render_template

from app import app

from user.views import read_dashboard_login_user

# view function to display all the recipes
@app.get('/dashboard/recipes/')
async def display_dashboard_recipes():
  """
  View function to display
  all the recipes
  """
  
  # set the respective endpoint url
  recipes_endpoint_url = "http://{0}:{1}/api/v1/recipes".format(
    os.environ.get('API_URL'),
    os.environ.get('API_PORT')
  )
  
  # get the logged in user's bearer token
  #app.logger.debug("HEADERS", request.headers.get('Authorization'))
  #headers = request.headers.get('Authorization')
  #app.logger.debug("AUTHORIZATION", headers)
  #token = headers.split()[1]
  
  app.logger.debug(session['token'])
  
  # get a reponse from the request
  response = urllib3.request(
    method="GET",
    url=recipes_endpoint_url,
    #headers={"Authorization": "Bearer " + session['token']}
  )
  
  # convert the returned response to json
  recipes = response.json()
  
  return render_template('recipe/display_recipes.html', recipes=recipes)
