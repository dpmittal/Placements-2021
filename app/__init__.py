import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask, request, render_template, flash, redirect, url_for, session, Blueprint
from functools import wraps
import requests
import json

app = Flask(__name__, instance_path=os.path.join(os.path.abspath(os.curdir), 'instance'), instance_relative_config=True, static_url_path="", static_folder="static")
app.config.from_pyfile('config.cfg')

# Importing Blueprints
from app.views.main import main

# Registering Blueprints

app.register_blueprint(main)