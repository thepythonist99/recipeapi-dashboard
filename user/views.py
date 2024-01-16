"""
Views for the user module
"""

import os
import urllib3

from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask import session

from app import app
from security import login_user


# # function to display the register view
# @app.get("/dashboard/user/register", response_class=HTMLResponse, tags=["user"])
# async def read_dashboard_register(request: Request):
#   """
#   View function to display the
#   register user template
#   """
  
#   # # get the respective endpoint url
#   # register_endpoint_url = "http://{0}/api/v1/users".format(
#   #   os.environ.get('API_URL')
#   # )
  
#   # # open the register endpoint url
#   # response = urlopen(url=register_endpoint_url)

#   return templates.TemplateResponse(
#     name="user/register.html",
#     context={'request': request}
#   )
  
# view function to display the login page
@app.get('/dashboard/user/login/')
async def read_dashboard_login():
  """
  View function to display the
  login user template
  """
  
  # display the login page
  return render_template('user/display_login.html')

# view function to login a user
@app.post('/dashboard/user/login/')
async def read_dashboard_login_user():
  """
  View function to login a user
  """
  
  # get the user credentials from the form
  user_username = request.form.get('username')
  user_password = request.form.get('password')
  
  # attempt a login
  login_attempt = await login_user(username=user_username, password=user_password)
  
  # check if the login parameters are present
  if "access_token" and "token_type" in login_attempt:
    # redirect the user to the main dashboard page
    app.logger.info("User successfully logged in.")
    #redirect_to = redirect(url_for('display_dashboard'))
    #redirect_to.headers['headers'] = login_attempt['access_token']
    session['token'] = login_attempt['access_token']
    return redirect(url_for('display_dashboard'))
    #return redirect_to
  
  else:
    app.logger.error(login_attempt['detail'])
    return redirect(url_for('read_dashboard_login'))
