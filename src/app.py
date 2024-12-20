from flask import Flask, request
import json
import requests
import sys
import os

app = Flask(__name__)

@app.get("/posts")
def get_all_posts():
    return [
        {
            "id":1,
            "tittle":"hello",
            "body":"world",
            "userId":1
        }
    ]

print(f"Running json Server on port {os.getenv('PORT')}")