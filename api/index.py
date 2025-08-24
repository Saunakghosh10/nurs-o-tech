from flask import Flask
import sys
import os

# Add the parent directory to Python path to import the main app
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the Flask app from the parent directory
from app import app

# For Vercel, we need to return the app for serverless function
def handler(event, context):
    return app(event, context)
