"""
Views for the dashboard module
"""
import flask

from flask import request
from flask import session
from flask import render_template

from app import app


# view function to display all the recipes
@app.get('/dashboard/')
async def display_dashboard():
  """
  View function to main
  dashboard page
  """
  
  return render_template('dashboard/display_dashboard.html')
