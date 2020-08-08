import random
import string
import gspread
import pprint
from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask, request, render_template, flash, redirect, url_for, session, Blueprint
from app import *

main = Blueprint('main', __name__)

scope = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(os.environ['GOOGLE_APPLICATION_CREDENTIALS'], scope)
client = gspread.authorize(creds)

@main.route('/')
def home():
    sheet = client.open('Thapar Placements 2021 Batch').sheet1
    data = sheet.get_all_records()
    data.pop(0)
    return render_template("landing.html", records = data)