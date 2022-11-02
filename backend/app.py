import os
from flask import Flask, render_template, request, url_for, redirect
from sqlalchemy.sql import func
from backend import app

basedir = os.path.abspath(os.path.dirname(__file__))

@app.route('/')
def index():
    return "Hello there!"
